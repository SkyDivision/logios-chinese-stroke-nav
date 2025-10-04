"""
Logios Chinese Stroke Navigator - Core Engine
Main stroke matching and character search functionality
"""

import json
import os
from typing import List, Dict, Set

class StrokeNavigator:
    def __init__(self, data_dir: str = "data"):
        """Initialize the stroke navigation system"""
        self.data_dir = data_dir
        self.characters = self._load_characters()
        self.radicals = self._load_radicals()
        
        # Stroke type mappings
        self.stroke_map = {
            'h': '横',    # héng
            's': '竖',    # shù
            'p': '撇',    # piě
            'n': '捺',    # nà
            'z': '折',    # zhé
        }
    
    def _load_characters(self) -> Dict:
        """Load character data from JSON"""
        try:
            with open(os.path.join(self.data_dir, 'characters.json'), 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _load_radicals(self) -> Dict:
        """Load radical data from JSON"""
        try:
            with open(os.path.join(self.data_dir, 'radicals.json'), 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def find_by_strokes(self, stroke_pattern: List[str]) -> List[Dict]:
        """
        Find characters matching a stroke pattern
        
        Args:
            stroke_pattern: List of stroke codes (e.g., ['h', 's', 'p'])
            
        Returns:
            List of matching characters with details
        """
        matches = []
        
        for char_id, char_data in self.characters.items():
            if 'strokes' not in char_data:
                continue
                
            char_strokes = char_data['strokes']
            
            # Check if stroke pattern matches
            if self._match_stroke_pattern(char_strokes, stroke_pattern):
                matches.append({
                    'character': char_data['char'],
                    'pinyin': char_data.get('pinyin', ''),
                    'meaning': char_data.get('meaning', ''),
                    'stroke_count': len(char_strokes),
                    'strokes': char_strokes
                })
        
        return matches
    
    def _match_stroke_pattern(self, char_strokes: List[str], pattern: List[str]) -> bool:
        """Check if character strokes match the search pattern"""
        if len(pattern) > len(char_strokes):
            return False
            
        # Convert stroke codes to Chinese names for matching
        pattern_strokes = [self.stroke_map.get(p, p) for p in pattern]
        char_strokes_full = char_strokes[:len(pattern_strokes)]
        
        return pattern_strokes == char_strokes_full
    
    def get_stroke_help(self) -> str:
        """Get help information about stroke types"""
        help_text = "Stroke Types Guide:\n"
        for code, name in self.stroke_map.items():
            help_text += f"  {code} - {name}\n"
        return help_text

# Example usage
if __name__ == "__main__":
    navigator = StrokeNavigator()
    print("Logios Stroke Navigator - Ready!")
    print(navigator.get_stroke_help())
