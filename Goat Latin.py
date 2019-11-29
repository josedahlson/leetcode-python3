class Solution:
    def toGoatLatin(self, S: str) -> str:
        S_split = S.split()
        new_list = []
        for i in range(len(S_split)):
            if S_split[i][0].lower() in "aeiou":
                new_str = S_split[i] + "ma" + (i+1)*"a"
                new_list.append(new_str)
            else:
                new_str = S_split[i][1:] + S_split[i][0] + "ma" + (i+1)*"a"
                new_list.append(new_str)
            i += 1

        return " ".join(new_list)
