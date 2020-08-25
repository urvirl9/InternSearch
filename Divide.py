def divide(dividend, divisor): 
quotient = 0;
temp = 0;

for i in range(31, -1, -1):
  if (temp + (divisor << i) <= dividend):
  temp += divisor << i;
  quotient |= 1 << i;
