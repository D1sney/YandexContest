def main():
    import sys
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)
    # Convert N to binary without the '0b' prefix
    s = bin(N)[2:]
    max_val = 0
    # Generate all cyclic rotations and track the maximum
    for i in range(len(s)):
        # Rotate right by i: last i bits to the front
        rotated = s[-i:] + s[:-i]
        # Convert back to integer
        val = int(rotated, 2)
        if val > max_val:
            max_val = val
    print(max_val)

if __name__ == "__main__":
    main()