#opening files
endings = open('/Users/Jakub/endings.txt', 'r')
skeleton = open('/Users/Jakub/skeleton_SamuraiShowdown.txt')

#declaring lists
rhythms_list = []
endings_list = []
beats_list = []

def iterate_skeleton(skeleton):
    """Function iterate skeleton has one parameter - skeleton text file with
    prefixes, beats and ending words of the song. Items of 
    each line are saved in variables while doing
    for loop. Next we distinguish between lines with
     or without XXX at the end. When processing lines without XXX we
    need to find out number of beats for this line and find number of beats of 
    ending words, which we can find in
    endings file. When processing XXX line we calculate number of beats we need 
    to complete the line and lookup
    for this number and rhyme in endings file. This is done by finding possible 
    indexex of both rhymes and and beats in
    endings file and then choosing intersect between them. Final lines are appended 
    to final song list and returned."""

    for sentence in skeleton:
        sentence = sentence.rstrip('\n')
        sen_list = sentence.split('::')
        ending_word = sen_list[-1]
        beats_sentence = int(sen_list[-2])
        prefix = sen_list[-3]
        if ending_word.endswith('XXX'):
            beats_needed = full_beats - beats_sentence
            beats_index = [i for i, x in enumerate(beats_list) if x == beats_needed]
            rhythm_index = [i for i, x in enumerate(rhythms_list) if x in last_ending_word]
            intersect = set(rhythm_index).intersection(beats_index)
            intersect = max(intersect)
            xxx_line = (str(prefix +' '+str(endings_list[intersect])))
            final_song.append(xxx_line)

        else:
            if ending_word != '':
                full_words_index = endings_list.index(ending_word)
                endings_beats = beats_list[full_words_index]
                full_beats = beats_sentence + endings_beats
                last_ending_word = ending_word
                final_song.append(str(prefix)+' '+str(ending_word))
            else:
                final_song.append(str(prefix)+ ' ' +str(ending_word))
    return final_song

def iterate_endings(endings):
    """Function takes one parameter - endings txt file with beats, endings, and rhythms. We iterate though file
    and prepare individual lists for each variable. Function does not return anything. """
    for sen in endings:
        sen = sen.rstrip('\n')
        sen_split = sen.split('::')
        beats = int(sen_split[2])
        ending = sen_split[0]
        rhythm = sen_split[1]
        rhythms_list.append(rhythm)
        endings_list.append(ending)
        beats_list.append(int(beats))


def main_function():
    """Function takes no parameters - first iterate_endings function is run to prepare lists for next processing.
    Next we store final string of the song in xxx_replace_list and iterate though this list while cleaning and
    concatenating each line. Result are complete lyrics of the song. """
    final_str = ''
    xxx_replace_list = []
    iterate_endings(endings)
    xxx_replace_list = iterate_skeleton(skeleton)
    for line in  xxx_replace_list:
        final_str = (final_str+line.lstrip('\'').lstrip(' ').rstrip(',') +'\n')
    return final_str

print main_function()



