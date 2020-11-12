\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 x11 + 0 x12 + x13 + 2 x14 + x15 + 3 x21 + 2 x22 + x23 + 0 x24 + 3 x25
   + 0 x31 + x32 + 0 x33 + 3 x34 + x35 + 4 x41 + x42 + x43 + 0 x44 + x45
   + 3 x51 + 2 x52 + 0 x53 + 0 x54 + 0 x55 + x61 + 5 x62 + x63 + 0 x64
   + 0 x65
Subject To
 Flight_0: x13 + x14 + x15 = 1
 Flight_1: x21 + x22 + x23 + x25 = 1
 Flight_2: x32 + x34 + x35 = 1
 Flight_3: x41 + x42 + x43 + x45 = 1
 Flight_4: x51 + x52 = 1
 Flight_5: x61 + x62 + x63 = 1
 Gate_1T_1: <= 1
 Gate_2T_1: <= 1
 Gate_3T_1: x13 <= 1
 Gate_4T_1: x14 <= 1
 Gate_5T_1: x15 <= 1
 Gate_1T_2: x21 <= 1
 Gate_2T_2: x22 <= 1
 Gate_3T_2: x13 + x23 <= 1
 Gate_4T_2: x14 <= 1
 Gate_5T_2: x15 + x25 <= 1
 Gate_1T_3: x21 + x41 <= 1
 Gate_2T_3: x22 + x32 + x42 <= 1
 Gate_3T_3: x23 + x43 <= 1
 Gate_4T_3: x34 <= 1
 Gate_5T_3: x25 + x35 + x45 <= 1
 Gate_1T_4: x21 + x41 <= 1
 Gate_2T_4: x22 + x32 + x42 <= 1
 Gate_3T_4: x23 + x43 <= 1
 Gate_4T_4: x34 <= 1
 Gate_5T_4: x25 + x35 + x45 <= 1
 Gate_1T_5: x41 + x51 <= 1
 Gate_2T_5: x32 + x42 + x52 <= 1
 Gate_3T_5: x43 <= 1
 Gate_4T_5: x34 <= 1
 Gate_5T_5: x35 + x45 <= 1
 Gate_1T_6: x61 <= 1
 Gate_2T_6: x62 <= 1
 Gate_3T_6: x63 <= 1
 Gate_4T_6: <= 1
 Gate_5T_6: <= 1
Bounds
Binaries
 x11 x12 x13 x14 x15 x21 x22 x23 x24 x25 x31 x32 x33 x34 x35 x41 x42 x43
 x44 x45 x51 x52 x53 x54 x55 x61 x62 x63 x64 x65
End
