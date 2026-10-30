# Runtime: 7 ms
# Memory: 15 MB

class Solution(object):
    def lemonadeChange(self, bills):
        bank = {5: 0, 10: 0, 20: 0}

        for i in bills:
            if i == 5:
                bank[5] += 1

            elif i == 10:
                if bank[5] < 1:
                    return False

                bank[5] -= 1
                bank[10] += 1

            elif i == 20:
                if bank[5] >= 1 and bank[10] >= 1:
                    bank[5] -= 1
                    bank[10] -= 1

                elif bank[5] >= 3:
                    bank[5] -= 3

                else:
                    return False

                bank[20] += 1

        return True