"""
Logios Chinese Stroke Navigator - Data Management
Handles character data loading, validation, and processing
"""

import json
import os
from typing import Dict, List, Optional

class DataManager:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.ensure_data_directory()
    
    def ensure_data_directory(self) -> None:
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            print(f"Created data directory: {self.data_dir}")
    
    def load_json_data(self, filename: str) -> Dict:
        """Load JSON data from file with error handling"""
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Data file not found: {filename}")
            return {}
        except json.JSONDecodeError:
            print(f"Invalid JSON in file: {filename}")
            return {}
    
    def save_json_data(self, filename: str, data: Dict) -> bool:
        """Save data to JSON file"""
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error saving {filename}: {e}")
            return False
    
    def validate_character_data(self, character_data: Dict) -> List[str]:
        """Validate character data structure"""
        errors = []
        
        required_fields = ['char', 'strokes', 'pinyin', 'meaning']
        
        for char_id, data in character_data.items():
            for field in required_fields:
                if field not in data:
                    errors.append(f"Character {char_id} missing field: {field}")
            
            # Validate strokes are list of strings
            if 'strokes' in data and not isinstance(data['strokes'], list):
                errors.append(f"Character {char_id} strokes should be a list")
        
        return errors
    
    def get_character_stats(self, character_data: Dict) -> Dict:
        """Get statistics about character data"""
        if not character_data:
            return {}
        
        total_chars = len(character_data)
        stroke_counts = {}
        radical_counts = {}
        
        for char_id, data in character_data.items():
            # Count by stroke number
            stroke_count = len(data.get('strokes', []))
            stroke_counts[stroke_count] = stroke_counts.get(stroke_count, 0) + 1
            
            # Count by radical (if available)
            radical = data.get('radical', 'unknown')
            radical_counts[radical] = radical_counts.get(radical, 0) + 1
        
        return {
            'total_characters': total_chars,
            'stroke_distribution': stroke_counts,
            'radical_distribution': radical_counts
        }

# Example usage
if __name__ == "__main__":
    dm = DataManager()
    print("Data Manager - Ready!")
    print(f"Data directory: {os.path.abspath(dm.data_dir)}")
