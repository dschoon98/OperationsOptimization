\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x11 + 2 x12 + 3 x13 + 3 x14 + 2 x21 + x22 + 4 x23 + 3 x24 + x31 + 3 x32
   + 4 x33 + 2 x34 + x41 + 3 x42 + 4 x43 + 2 x44 + x51 + 3 x52 + x53
   + 3 x54
Subject To
 Flight_1: x11 + x12 + x13 + x14 = 1
 Flight_2: x21 + x22 + x23 + x24 = 1
 Flight_3: x31 + x32 + x33 + x34 = 1
 Flight_4: x41 + x42 + x43 + x44 = 1
 Flight_5: x51 + x52 + x53 + x54 = 1
 Gate_1T_1: x11 <= 1
 Gate_2T_1: x12 <= 1
 Gate_3T_1: x13 <= 1
 Gate_4T_1: x14 <= 1
 Gate_1T_2: x11 <= 1
 Gate_2T_2: x12 <= 1
 Gate_3T_2: x13 <= 1
 Gate_4T_2: x14 <= 1
 Gate_1T_3: x11 <= 1
 Gate_2T_3: x12 <= 1
 Gate_3T_3: x13 <= 1
 Gate_4T_3: x14 <= 1
 Gate_1T_4: x11 + x21 <= 1
 Gate_2T_4: x12 + x22 <= 1
 Gate_3T_4: x13 + x23 <= 1
 Gate_4T_4: x14 + x24 <= 1
 Gate_1T_5: x11 + x21 <= 1
 Gate_2T_5: x12 + x22 <= 1
 Gate_3T_5: x13 + x23 <= 1
 Gate_4T_5: x14 + x24 <= 1
 Gate_1T_6: x11 + x21 <= 1
 Gate_2T_6: x12 + x22 <= 1
 Gate_3T_6: x13 + x23 <= 1
 Gate_4T_6: x14 + x24 <= 1
 Gate_1T_7: x11 + x21 <= 1
 Gate_2T_7: x12 + x22 <= 1
 Gate_3T_7: x13 + x23 <= 1
 Gate_4T_7: x14 + x24 <= 1
 Gate_1T_8: x21 + x31 + x41 <= 1
 Gate_2T_8: x22 + x32 + x42 <= 1
 Gate_3T_8: x23 + x33 + x43 <= 1
 Gate_4T_8: x24 + x34 + x44 <= 1
 Gate_1T_9: x21 + x31 + x41 <= 1
 Gate_2T_9: x22 + x32 + x42 <= 1
 Gate_3T_9: x23 + x33 + x43 <= 1
 Gate_4T_9: x24 + x34 + x44 <= 1
 Gate_1T_10: x21 + x31 + x41 <= 1
 Gate_2T_10: x22 + x32 + x42 <= 1
 Gate_3T_10: x23 + x33 + x43 <= 1
 Gate_4T_10: x24 + x34 + x44 <= 1
 Gate_1T_11: x21 + x31 + x41 <= 1
 Gate_2T_11: x22 + x32 + x42 <= 1
 Gate_3T_11: x23 + x33 + x43 <= 1
 Gate_4T_11: x24 + x34 + x44 <= 1
 Gate_1T_12: x21 + x31 + x41 <= 1
 Gate_2T_12: x22 + x32 + x42 <= 1
 Gate_3T_12: x23 + x33 + x43 <= 1
 Gate_4T_12: x24 + x34 + x44 <= 1
 Gate_1T_13: x21 + x31 + x41 <= 1
 Gate_2T_13: x22 + x32 + x42 <= 1
 Gate_3T_13: x23 + x33 + x43 <= 1
 Gate_4T_13: x24 + x34 + x44 <= 1
 Gate_1T_14: x21 + x31 + x41 <= 1
 Gate_2T_14: x22 + x32 + x42 <= 1
 Gate_3T_14: x23 + x33 + x43 <= 1
 Gate_4T_14: x24 + x34 + x44 <= 1
 Gate_1T_15: x21 + x31 + x41 <= 1
 Gate_2T_15: x22 + x32 + x42 <= 1
 Gate_3T_15: x23 + x33 + x43 <= 1
 Gate_4T_15: x24 + x34 + x44 <= 1
 Gate_1T_16: x31 + x41 + x51 <= 1
 Gate_2T_16: x32 + x42 + x52 <= 1
 Gate_3T_16: x33 + x43 + x53 <= 1
 Gate_4T_16: x34 + x44 + x54 <= 1
 Gate_1T_17: x31 + x41 + x51 <= 1
 Gate_2T_17: x32 + x42 + x52 <= 1
 Gate_3T_17: x33 + x43 + x53 <= 1
 Gate_4T_17: x34 + x44 + x54 <= 1
 Gate_1T_18: x31 + x41 + x51 <= 1
 Gate_2T_18: x32 + x42 + x52 <= 1
 Gate_3T_18: x33 + x43 + x53 <= 1
 Gate_4T_18: x34 + x44 + x54 <= 1
Bounds
Binaries
 x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34 x41 x42 x43 x44 x51 x52
 x53 x54
End
