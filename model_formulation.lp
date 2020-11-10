\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  x[1,1] + 2 x[1,2] + 3 x[1,3] + 4 x[1,4] + 5 x[2,1] + 6 x[2,2] + 7 x[2,3]
   + 8 x[2,4] + 9 x[3,1] + 10 x[3,2] + 11 x[3,3] + 12 x[3,4] + 13 x[4,1]
   + 14 x[4,2] + 15 x[4,3] + 16 x[4,4]
Subject To
 Flight_1: x[1,1] + x[1,2] + x[1,3] + x[1,4] = 1
 Flight_2: x[2,1] + x[2,2] + x[2,3] + x[2,4] = 1
 Flight_3: x[3,1] + x[3,2] + x[3,3] + x[3,4] = 1
 Gate_1: x[1,1] + x[2,1] + x[3,1] + x[4,1] <= 1
 Gate_2: x[1,2] + x[2,2] + x[3,2] + x[4,2] <= 1
 Gate_3: x[1,3] + x[2,3] + x[3,3] + x[4,3] <= 1
Bounds
Binaries
 x[1,1] x[1,2] x[1,3] x[1,4] x[2,1] x[2,2] x[2,3] x[2,4] x[3,1] x[3,2]
 x[3,3] x[3,4] x[4,1] x[4,2] x[4,3] x[4,4]
End
