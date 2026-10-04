"""

--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1907/B -----------------


Polycarp has a problem — his laptop keyboard is broken.

Now, when he presses the 'b' key, it acts like an unusual backspace: it deletes the last (rightmost) lowercase letter in the typed string. If there are no lowercase letters in the typed string, then the press is completely ignored.

Similarly, when he presses the 'B' key, it deletes the last (rightmost) uppercase letter in the typed string. If there are no uppercase letters in the typed string, then the press is completely ignored.

In both cases, the letters 'b' and 'B' are not added to the typed string when these keys are pressed.

Consider an example where the sequence of key presses was "ARaBbbitBaby". In this case, the typed string will change as follows:
 "" →A "A" →R "AR" →a "ARa" →B "Aa" →b "A" →b "A" →i "Ai" →t "Ait" →B "it" →a "ita" →b "it" →y "ity".

Given a sequence of pressed keys, output the typed string after processing all key presses.

Input
The first line of the input data contains an integer t (1 ≤ t ≤ 1000), the number of test cases in the test.

The following contains t non-empty lines, which consist of lowercase and uppercase letters of the Latin alphabet.

It is guaranteed that each line contains at least one letter and the sum of the lengths of the lines does not exceed 10^6.

Output
For each test case, output the result of processing the key presses on a separate line. If the typed string is empty, then output an empty line.

Input:
12
ARaBbbitBaby
YetAnotherBrokenKeyboard
Bubble
Improbable
abbreviable
BbBB
BusyasaBeeinaBedofBloomingBlossoms
CoDEBARbIES
codeforces
bobebobbes
b
TheBBlackbboard

Output:
ity
YetnotherrokenKeoard
le
Imprle
revile

usyasaeeinaedofloominglossoms
CDARIES
codeforces
es

helaoard
"""
cases = int(input())
for _ in range(cases):
    s = input()
    need_lower = 0
    need_upper = 0
    ans = []

    for c in reversed(s):
        if c == 'b':
            need_lower += 1
        elif c == 'B':
            need_upper += 1
        elif c.islower():
            if need_lower > 0:
                need_lower -= 1
            else:
                ans.append(c)
        else:  # uppercase letter
            if need_upper > 0:
                need_upper -= 1
            else:
                ans.append(c)

    print(''.join(reversed(ans)))
    print("-------------------")