import sqlite3
import re
import Levenshtein

class TagsRepo:
    def __init__(self):
        self.conn = sqlite3.connect('db/tags.sqlite3')
        self.cur = self.conn.cursor()
        self.search_threshold = 10
    
    def find_most_relevant(self, search_tag):
        search_text = self._clean_search_text(search_tag)
        all_tags = self._get_all_tags()
        matching_tags = self._get_matching_tags(search_text, all_tags)
        
        if matching_tags:
            return self._get_full_row_by_best_match(matching_tags)
        else:
            return None
    
    def _clean_search_text(self, search_tag):
        return re.sub(r'[^a-zA-Z0-9]', '', search_tag)
    
    def _get_all_tags(self):
        self.cur.execute("SELECT id, search_tag FROM tags")
        return self.cur.fetchall()
    
    def _get_matching_tags(self, search_text, all_tags):
        matching_tags = []
        for tag in all_tags:
            distance = Levenshtein.distance(search_text, str(tag[1]))
            if distance <= self.search_threshold:
                matching_tags.append((tag, distance))
        return matching_tags
    
    def _get_full_row_by_best_match(self, matching_tags):
        best_match = min(matching_tags, key=lambda x: x[1])
        best_match_id = best_match[0][0]
        
        query = ("SELECT full_tag, tag, lens_size, bridge_size, "
                "shackle_length, earpiece_length "
                "FROM tags WHERE id=?")
        self.cur.execute(query, (best_match_id,))

        full_row = self.cur.fetchone()
        columns = [column[0] for column in self.cur.description]
        return dict(zip(columns, full_row))
    
    def close(self):
        self.cur.close()
        self.conn.close()