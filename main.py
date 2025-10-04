"""
Logios Chinese Stroke Navigator - Main Interface
User-friendly interface for stroke-based character search
"""

import os
import sys
from stroke_navigator import StrokeNavigator
from data_manager import DataManager

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the beautiful application banner"""
    banner = """
    ╔═══════════════════════════════════════════════╗
    ║           笔画导航 - Logios Chinese Stroke Navigator    ║
    ║         Find Chinese characters by strokes!          ║
    ║         Sky Division & Logios, 2025                 ║
    ╚═══════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Main application loop"""
    # Initialize our systems
    data_manager = DataManager()
    navigator = StrokeNavigator()
    
    while True:
        clear_screen()
        print_banner()
        
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("1. 🔍 Search characters by strokes")
        print("2. 📚 View stroke types guide") 
        print("3. ℹ️  About this project")
        print("4. 🚪 Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            search_by_strokes(navigator)
        elif choice == '2':
            show_stroke_guide(navigator)
        elif choice == '3':
            show_about()
        elif choice == '4':
            print("\n谢谢! Thank you for using Logios Stroke Navigator! 👋")
            break
        else:
            input("\nInvalid choice! Press Enter to continue...")

def search_by_strokes(navigator):
    """Search characters using stroke patterns"""
    clear_screen()
    print("🔍 STROKE SEARCH")
    print("="*30)
    
    print("\nEnter stroke types (one by one):")
    print("h: 横(héng)  s: 竖(shù)  p: 撇(piě)")
    print("n: 捺(nà)    z: 折(zhé)")
    print("\nExample: 'h s p' for 横竖撇")
    
    stroke_input = input("\nEnter strokes (space separated): ").strip().lower()
    
    if not stroke_input:
        input("\nNo strokes entered! Press Enter to continue...")
        return
    
    stroke_pattern = stroke_input.split()
    
    # Validate stroke codes
    valid_strokes = ['h', 's', 'p', 'n', 'z']
    invalid_strokes = [s for s in stroke_pattern if s not in valid_strokes]
    
    if invalid_strokes:
        print(f"\n❌ Invalid stroke codes: {invalid_strokes}")
        print("Please use only: h, s, p, n, z")
        input("\nPress Enter to continue...")
        return
    
    print(f"\n🔎 Searching for pattern: {' → '.join(stroke_pattern)}...")
    
    # Perform search
    matches = navigator.find_by_strokes(stroke_pattern)
    
    # Display results
    clear_screen()
    print("📊 SEARCH RESULTS")
    print("="*40)
    print(f"Pattern: {' → '.join(stroke_pattern)}")
    print(f"Found {len(matches)} matching characters")
    print("="*40)
    
    if matches:
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match['character']} - {match['pinyin']}")
            print(f"   Meaning: {match['meaning']}")
            print(f"   Strokes: {match['stroke_count']} total")
            print()
    else:
        print("\n❌ No characters found matching that stroke pattern.")
        print("Try a different pattern or check the stroke guide!")
    
    input("\nPress Enter to return to menu...")

def show_stroke_guide(navigator):
    """Display stroke types guide"""
    clear_screen()
    print("📚 STROKE TYPES GUIDE")
    print("="*35)
    print(navigator.get_stroke_help())
    print("\n💡 Tip: Characters are built from these basic strokes!")
    input("\nPress Enter to return to menu...")

def show_about():
    """Display about information"""
    clear_screen()
    print("ℹ️  ABOUT LOGIOS STROKE NAVIGATOR")
    print("="*45)
    print("\nAn intelligent Chinese character learning system")
    print("that helps you find characters by their strokes!")
    print("\n🌟 Features:")
    print("  • Stroke-based character search")
    print("  • Radical intelligence")
    print("  • Learning-focused design")
    print("  • Open source and free!")
    print("\n🎯 Perfect for:")
    print("  • Chinese language learners")
    print("  • Character recognition practice")
    print("  • Stroke order learning")
    print(f"\n📁 Data directory: {os.path.abspath('data')}")
    print("\nBuilt with 心 by Sky Division & Logios, 2025")
    input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n谢谢! Thanks for using Logios! 👋")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please make sure the data files are available.")
