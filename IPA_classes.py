
class IpaSym:

    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
  
    @staticmethod
    def VC_checker(word):
        for i in word:
            if isinstance(i, Consonant):
                print("'{}' is a consonant".format(i.symbol))
            else:
                print("'{}' is a vowel".format(i.symbol))


    @staticmethod
    def word_initial_check(syllables):

        three_c_clusters = ["spl", "spr", "str", "skr", "skw"]
        two_c_clusters = ["sm", "sn", "st", "sw", "sk", "sl", "sp", "sf", "θw",
                          "dw", "tw", "θr", "dr", "tr", "kw", "kr", "kl", "pr",
                          "fr", "br", "gr", "pl", "fl", "bl", "gl", "ʃr"]

        vowels = "iɪeæəʌɚuɔʊɑ"
        syl_num = len(syllables)
        for j in range(1, syl_num):
            sound_num = len(syllables[j])
            syllable = syllables[j]
            cluster = ""
            for k in range(sound_num):
                if syllable[k] in vowels:
                    break
                else:
                    cluster += syllable[k]
            cluster_len = len(cluster)
            three_c = False
            temp_syll = syllables[j]
            if cluster_len >= 3:
                m = cluster_len
                while m >= 3:
                    if cluster not in three_c_clusters and cluster_len >= 3:
                        syllables[j-1] += cluster[0]
                        syllables[j] = temp_syll[1:sound_num]
                        temp_syll = temp_syll[1:sound_num]
                        cluster = cluster[1:]
                    elif cluster in three_c_clusters:
                        three_c = True
                    m -= 1
            if cluster not in two_c_clusters and three_c == False and len(cluster) > 1:
                syllables[j-1] += cluster[0]
                syllables[j] = temp_syll[1:sound_num]
        return syllables

    @staticmethod
    def basic_syllabification(word):
        all_syllables = []
        syllable = ""
        for el in word:
            if isinstance(el, Consonant):
                syllable += el.symbol
            else:
                syllable += el.symbol
                all_syllables.append(syllable)
                syllable = ""
        last_syll = all_syllables[-1]
        num = -1
        cons_to_add = ""
        while num >= -5:
            if not isinstance(word[num], Consonant):
                cons_to_add = cons_to_add[::-1]
                last_syll += cons_to_add
                all_syllables[-1] = last_syll
                break
            else:
                cons_to_add += word[num].symbol
            num -= 1
        return all_syllables

    @staticmethod
    def is_sonorous(post_mop):
        sonority_syllables = []
        part = ""
        for sound in post_mop:
            if sound == ".":
                sonority_syllables.append(part)
                part = ""
            else:
                part += str(sound.value)

        print(sonority_syllables)

        pre_vowel_sets = []        
        for set_of_numbers in sonority_syllables:
            pre_vowel = ""
            for number in set_of_numbers:
                if int(number) == 8:
                    break
                else:
                    pre_vowel += number
            pre_vowel_sets.append(pre_vowel)
        post_vowel_sets = []
        for set_of_numbers in sonority_syllables:
            part_left = set_of_numbers
            for num in set_of_numbers:
                if int(num) != 8:
                    part_left = part_left[1:]
                elif int(num) == 8:
                    post_vowel_sets.append(part_left[1:])
                    break
        print(pre_vowel_sets)
        print(post_vowel_sets)
        sonority = True
        verify_sonority = []
        for seq in pre_vowel_sets:
            if len(seq) > 1:
                first_pair = seq[0] < seq[1]
                if first_pair == False:
                    sonority = False   
                    if len(seq) == 3 and first_pair == True:
                        second_pair = seq[1] < seq[2]
                        if second_pair == False:
                            sonority = False
            verify_sonority.append(sonority)
            sonority = True
        for sequence in post_vowel_sets:
            if len(sequence) > 1:
                f_pair = sequence[0] > sequence[1]
                if f_pair == False:
                    sonority = False
                    if len(sequence) >= 3 and f_pair == True:
                        s_pair = sequence[1] > sequence[2]
                        if s_pair == False:
                            sonority = False
                            if len(sequence) >= 4 and s_pair == True:
                                t_pair = sequence[2] > sequence[3]
                                if t_pair == False:
                                    sonority = False
                                    if len(sequence) == 5 and t_pair == True:
                                        fourth_pair = sequence[3] > sequence[4]
                                        if fourth_pair == False:
                                            sonority = False
            verify_sonority.append(sonority)
            sonority = True

        print(verify_sonority)
        if False in verify_sonority:
            print('ill')
            return 'ill-formed'
        else:
            print('good')
            return 'well-formed'

        
class Vowel(IpaSym):

    def __init__(self, symbol, value):
        super().__init__(symbol, value)


class Consonant(IpaSym):

    def __init__(self, symbol, value):
        super().__init__(symbol, value)

    @staticmethod
    def sonority_checker(ch1, ch2):
        return ch1.value > ch2.value


def sounds_to_obj_MOP(word):

    sound_dict = {
        ch_01: 'p', ch_02: 'b', ch_03: 't', ch_04: 'd', ch_05: 'k', ch_06: 'g', 
        ch_07: 'ʔ', ch_08: 'ʧ', ch_09: 'ʤ', ch_10: 'f', ch_11: 'v', ch_12: 'θ', 
        ch_13: 'ð', ch_14: 's', ch_15: 'z', ch_16: 'ʃ', ch_17: 'ʒ', ch_18: 'm', 
        ch_19: 'n', ch_20: 'ŋ', ch_21: 'r', ch_22: 'l', ch_23: 'ɾ', ch_24: 'w', 
        ch_25: 'j', ch_26: 'i', ch_27: 'ɪ', ch_28: 'e', ch_29: 'æ', ch_30: 'ə', 
        ch_31: 'ʌ', ch_32: 'ɚ', ch_33: 'u', ch_34: 'ɔ', ch_35: 'ʊ', ch_36: 'ɑ', ch_37: 'h'}
    list_of_obj = []
    for sound in word:
        for key, value in sound_dict.items(): 
            if sound == value: 
                list_of_obj.append(key)
    syllabified = IpaSym.basic_syllabification(list_of_obj)
    improved = IpaSym.word_initial_check(syllabified)
    return improved


def sounds_to_obj_SSG(word):
    sound_dict = {
        ch_01: 'p', ch_02: 'b', ch_03: 't', ch_04: 'd', ch_05: 'k', ch_06: 'g', 
        ch_07: 'ʔ', ch_08: 'ʧ', ch_09: 'ʤ', ch_10: 'f', ch_11: 'v', ch_12: 'θ', 
        ch_13: 'ð', ch_14: 's', ch_15: 'z', ch_16: 'ʃ', ch_17: 'ʒ', ch_18: 'm', 
        ch_19: 'n', ch_20: 'ŋ', ch_21: 'r', ch_22: 'l', ch_23: 'ɾ', ch_24: 'w', 
        ch_25: 'j', ch_26: 'i', ch_27: 'ɪ', ch_28: 'e', ch_29: 'æ', ch_30: 'ə', 
        ch_31: 'ʌ', ch_32: 'ɚ', ch_33: 'u', ch_34: 'ɔ', ch_35: 'ʊ', ch_36: 'ɑ', ch_37: 'h'}
    one_word = ""
    for item in word:
        if item == word[-1]:
            one_word += item
        else:
            one_word += item
            one_word += " "
    list_of_obj = []
    for sound in one_word:
        if sound == " ":
            list_of_obj.append('.')
        else:
            for key, value in sound_dict.items(): 
                if sound == value: 
                    list_of_obj.append(key)
    list_of_obj.append('.')
    is_it = IpaSym.is_sonorous(list_of_obj)
    return is_it


# ___Consonants___
ch_01 = Consonant("p", 1)
ch_02 = Consonant("b", 1)
ch_03 = Consonant("t", 1)
ch_04 = Consonant("d", 1)
ch_05 = Consonant("k", 1)
ch_06 = Consonant("g", 1)
ch_07 = Consonant("ʔ", 1)
ch_08 = Consonant("ʧ", 2)
ch_09 = Consonant("ʤ", 2)
ch_10 = Consonant("f", 3)
ch_11 = Consonant("v", 3)
ch_12 = Consonant("θ", 3)
ch_13 = Consonant("ð", 3)
ch_14 = Consonant("s", 3)
ch_15 = Consonant("z", 3)
ch_16 = Consonant("ʃ", 3)
ch_17 = Consonant("ʒ", 3)
ch_18 = Consonant("m", 4)
ch_19 = Consonant("n", 4)
ch_20 = Consonant("ŋ", 4)
ch_21 = Consonant("r", 5)
ch_22 = Consonant("l", 5)
ch_23 = Consonant("ɾ", 6)
ch_24 = Consonant("w", 7)
ch_25 = Consonant("j", 7)
ch_37 = Consonant("h", 3)
# ___Vowels___
ch_26 = Vowel("i", 8)
ch_27 = Vowel("ɪ", 8)
ch_28 = Vowel("e", 8)
ch_29 = Vowel("æ", 8)
ch_30 = Vowel("ə", 8)
ch_31 = Vowel("ʌ", 8)
ch_32 = Vowel("ɚ", 8)
ch_33 = Vowel("u", 8)
ch_34 = Vowel("ɔ", 8)
ch_35 = Vowel("ʊ", 8)
ch_36 = Vowel("ɑ", 8)

"""

vowel > glide > flap > liquid > nasal > fricative > affricate > plosive

plosive = "pbtdkgʔ"
nasal = "mnŋ"
tap_flap = "ɾ"
fricative = "fvθðszʃʒh"
liquid = "ɹl"
glide = "wj"
affricate = "ʧʤ"

"""