class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # to justify the words what need to do is maintain the curr line list
        # whenever len(curr_line_list) + wordCountInCurrLine + nextWord > maxWidth need next line
        # Justification is needed in that case, and to do that we will do 
        # maxwidth - (len(curr_line_list)  + wordCountInCurrLine - 1) those many extra spaces 
        # need to fill, and to do that we can do // to get how many spaces we need to fill? 
        # and % to extra space in intial
        # Make string and add to res list, rest curr_line_list = [], and wordCountInCurrLine= 0
        
        res = []
        curr_line = []
        word_count = 0  # Total length of words in current line

        for word in words:
            # If adding current word exceeds maxWidth, justify current line
            if word_count + len(curr_line) + len(word) > maxWidth:
                # Calculate spaces needed and distribute
                spaces = maxWidth - word_count
                gaps = len(curr_line) - 1

                # If multiple words, distribute spaces between them
                if len(curr_line) > 1:
                    base_spaces = spaces // gaps
                    extra = spaces % gaps
                    line = ""
                    for i, w in enumerate(curr_line[:-1]):
                        line += w + " " * (base_spaces + (1 if i < extra else 0))
                    line += curr_line[-1]
                else:
                    # Single word case - left justify
                    line = curr_line[0] + " " * spaces

                res.append(line)
                curr_line = []
                word_count = 0

            curr_line.append(word)
            word_count += len(word)

        # Handle last line (left-justified)
        last_line = " ".join(curr_line)
        res.append(last_line + " " * (maxWidth - len(last_line)))

        return res
