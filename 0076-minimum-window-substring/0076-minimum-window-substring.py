class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l1 = len(s)
        l2 = len(t)

        if l1 < l2:
            return ""

        h1 = {}
        h2 = Counter(t)

        # [window length, left index, right index]
        m = [float('inf'), 0, 0]

        i = 0

        # Number of different characters we need
        need = len(h2)

        # Number of different characters currently satisfied
        have = 0

        for j in range(l1):

            # Expand the window
            h1[s[j]] = h1.get(s[j], 0) + 1

            # This character has reached its required frequency
            if s[j] in h2 and h1[s[j]] == h2[s[j]]:
                have += 1

            # Window is valid, so try to make it smaller
            while have == need:

                win_size = j - i + 1

                # Save the smallest window
                if m[0] > win_size:
                    m = [win_size, i, j]

                # Remove leftmost character
                h1[s[i]] -= 1

                # We no longer have enough of this character
                if s[i] in h2 and h1[s[i]] < h2[s[i]]:
                    have -= 1

                # Move left pointer
                i += 1

        # No valid window found
        if m[0] == float('inf'):
            return ""

        return s[m[1]:m[2] + 1]