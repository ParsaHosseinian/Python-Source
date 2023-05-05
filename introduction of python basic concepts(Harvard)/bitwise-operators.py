# bitwise operators:

# &  AND

# |  OR 

# ^  XOR                   (Sets each bit to 1 if only one of two bits is 1)

# ~  NOT                   (Inverts all the bits) (استفاده از روش متمم دو برای منفی کردن اعداد در باینری) 
# (این روش بدین گونه است که از سمت راست اولین 1 رو دست نمی زنیم و بعد از اون رو همه بیت هارو تغییر میدیم)
# example: x = 3 , ~x = -4 ; actually means: ~x = -x-1

# << Zero fill left shift  (Shift left by pushing zeros in from the right and let the leftmost bits fall off)
# example: x << 1 actually means: x * 2 ** 1

# >> Signed right shift    (Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off)
# example: x >> 1  actually means: x // 2 ** 1 