import datetime
import itertools


class XorShift128Plus(object):
    def __init__(self):
        self.s0 = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.s1 = self.s0 // 2
        self.state = [self.s0, self.s1]

    def current_double(self):
        val = (self.s0 + self.s1) & 0x1fffffffffffff
        return float(val) / 2 ** 53

    # This function generates another 64-bit integer
    def __next__(self):
        s1 = self.state[0]
        s0 = self.state[1]

        self.state[0] = s0
        s1 ^= (s1 << 23)
        s1 &= 0xffffffffffffffff
        self.state[1] = s1 ^ s0 ^ (s1 >> 17) ^ (s0 >> 26)

        random_val = (self.state[1] + s0) & 0xffffffffffffffff

        return random_val

    # This function generates another floating point-type number in the range [0,1)
    def next_double(self):
        return float(next(self) & 0x1fffffffffffff) / 2 ** 53


def main():
    state1 = int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    state2 = state1//2
    prng = XorShift128Plus(state1, state2)
    for _ in itertools.repeat(None, 20):
        print(prng.next_double())


if __name__ == '__main__':
    main()
