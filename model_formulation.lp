\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 x11 + 0 x12 + 0 x13 + 0 x14 + 0 x15 + 0 x21 + 0 x22 + 0 x23 + 0 x24
   + 0 x25 + 0 x31 + 0 x32 + 0 x33 + 0 x34 + 0 x35 + 0 x41 + 0 x42 + 0 x43
   + 0 x44 + 0 x45 + 0 x11 + 0 x12 + 0 x13 + 0 x14 + 0 x15 + 0 x21 + 0 x22
   + 0 x23 + 0 x24 + 0 x25 + 0 x31 + 0 x32 + 0 x33 + 0 x34 + 0 x35 + 0 x41
   + 0 x42 + 0 x43 + 0 x44 + 0 x45 + x11 + 2 x12 + 3 x13 + 4 x14 + 4 x15
   + 5 x21 + 6 x22 + 7 x23 + 8 x24 + 8 x25 + 9 x31 + 10 x32 + 11 x33
   + 12 x34 + 12 x35 + 13 x41 + 14 x42 + 15 x43 + 16 x44 + 16 x45
Subject To
 Flight_1: x11 = 1
 Flight_2: x22 = 1
 Flight_3: x31 + x32 + x33 + x34 = 1
 Flight_4: x41 + x42 + x43 = 1
 Gate_1T_1: x11 <= 1
 Gate_2T_1: x22 <= 1
 Gate_3T_1: <= 1
 Gate_4T_1: <= 1
 Gate_5T_1: <= 1
 Gate_1T_2: x11 + x31 <= 1
 Gate_2T_2: x22 + x32 <= 1
 Gate_3T_2: x33 <= 1
 Gate_4T_2: x34 <= 1
 Gate_5T_2: <= 1
 Gate_1T_3: x31 + x41 <= 1
 Gate_2T_3: x32 + x42 <= 1
 Gate_3T_3: x33 + x43 <= 1
 Gate_4T_3: x34 <= 1
 Gate_5T_3: <= 1
Bounds
Binaries
 x11 x12 x13 x14 x15 x21 x22 x23 x24 x25 x31 x32 x33 x34 x35 x41 x42 x43
 x44 x45 x11 x12 x13 x14 x15 x21 x22 x23 x24 x25 x31 x32 x33 x34 x35 x41
 x42 x43 x44 x45 x11 x12 x13 x14 x15 x21 x22 x23 x24 x25 x31 x32 x33 x34
 x35 x41 x42 x43 x44 x45
End
