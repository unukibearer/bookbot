def main():
    with open('/home/unukibearer/workspace/USERNAME/bookbot/books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)
        words = file_contents.split()
        file_contents_string = str(file_contents)
        lower_file_context_string = file_contents_string.lower()
        char_count = {}
        for c in lower_file_context_string:
            if c.isalpha():
                if c in char_count:
                    char_count[c] += 1
                else:
                    char_count[c] = 1

        char_list = [{"char": k, "count": v} for k, v in char_count.items()]
        def sort_on(dict):
            return dict["char"]
    
        char_list.sort(key=sort_on)
        print("")
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        for item in char_list:
            print(f"The '{item['char']}' character was found {item['count']} times")
        print("--- End report ---")
        

            
            
        

main()