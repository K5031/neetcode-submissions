class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for segment in strs:
            l = len(segment)
            encoded_string += str(l) + "#" + segment

        return encoded_string

    def decode(self, s: str) -> List[str]:
        counter = 0
        decoded_string = []
        length = ""

        while counter < len(s):
            if s[counter] != "#":
                length += s[counter]
                counter += 1
            else:
                counter += 1
                string = ""
                for i in range(int(length)):
                    string += s[counter]
                    counter += 1
                length = ""
                decoded_string.append(string)

        return decoded_string