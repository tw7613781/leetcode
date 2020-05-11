# time limit exceed
# class Solution:
#     def isIdealPermutation(self, A):
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
#         for i in range(len(A)):
#             for j in range(i+2, len(A)):
#                 if A[i] > A[j]:
#                     return False
#         return True

class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = [0]*len(A)
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag[i] = 1
                if i>0:
                    if flag[i-1] == 1:
                        return False
            else:
                flag[i] = 0
        if A == sorted(A): return True
        else: return False


A = [1,0,2]
# A = [1,2,0]
# A = [2,1]
# A = [1,0,2,4,3,5,7,6,8,9,11,10,12,13,15,14,16,18,17,20,19,22,21,24,23,25,26,27,29,28,30,31,32,33,34,36,35,37,39,38,41,40,42,44,43,45,47,46,49,48,51,50,53,52,54,55,56,57,59,58,60,62,61,64,63,66,65,68,67,70,69,71,72,74,73,76,75,77,78,80,79,82,81,84,83,86,85,87,89,88,91,90,92,93,95,94,96,98,97,99,101,100,103,102,104,105,106,107,109,108,110,112,111,114,113,116,115,118,117,120,119,122,121,124,123,126,125,127,128,130,129,131,133,132,134,135,136,138,137,139,141,140,142,143,145,144,147,146,149,148,150,152,151,153,155,154,157,156,159,158,161,160,162,163,165,164,167,166,169,168,170,172,171,174,173,176,175,178,177,180,179,181,183,182,184,185,186,187,189,188,191,190,192,193,195,194,197,196,198,199,201,200,202,203,204,206,205,208,207,209,211,210,212,214,213,215,217,216,219,218,220,221,222,223,225,224,227,226,229,228,230,232,231,233,235,234,237,236,238,239,240,242,241,243,244,245,246,247,248,250,249,251,252,253,254,255,257,256,258,260,259,261,263,262,265,264,267,266,269,268,270,272,271,273,275,274,277,276,278,280,279,282,281,284,283,286,285,287,288,289,290,291,292,293,294,296,295,297,299,298,301,300,302,304,303,305,307,306,308,309,310,312,311,313,315,314,316,318,317,320,319,321,322,323,324,325,326,328,327,330,329,332,331,333,334,335,336,338,337,340,339,341,343,342,345,344,347,346,349,348,350,352,351,354,353,356,355,358,357,360,359,361,362,363,364,365,366,367,368,369,370,372,371,373,374,376,375,377,378,379,381,380,383,382,385,384,386,387,388,389,390,392,391,393,394,395,396,398,397,400,399,402,401,403,405,404,407,406,408,409,411,410,412,414,413,416,415,417,418,419,421,420,422,423,424,426,425,428,427,430,429,432,431,434,433,435,436,437,438,440,439,441,443,442,444,445,447,446,449,448,451,450,453,452,455,454,456,458,457,459,461,460,462,464,463,466,465,467,468,469,470,471,473,472,475,474,476,477,478,480,479,481,483,482,485,484,486,487,488,489,491,490,493,492,495,494,497,496,499,498,501,500,502,503,505,504,507,506,509,508,511,510,513,512,515,514,516,517,519,518,520,521,523,522,525,524,526,528,527,529,531,530,532,534,533,535,536,538,537,540,539,541,542,544,543,545,547,546,548,550,549,551,553,552,555,554,557,556,559,558,561,560,563,562,564,565,567,566,569,568,571,570,572,573,575,574,577,576,579,578,581,580,582,584,583,586,585,588,587,589,590,592,591,593,595,594,597,596,599,598,600,601,602,604,603,605,607,606,609,608,610,612,611,614,613,615,616,617,618,619,621,620,623,622,625,624,627,626,628,630,629,631,633,632,634,636,635,638,637,639,641,640,642,644,643,645,647,646,649,648,650,651,652,653,655,654,656,657,658,659,660,661,662,664,663,665,666,668,667,669,670,671,673,672,674,675,676,678,677,680,679,681,682,684,683,685,687,686,688,689,691,690,692,693,694,695,697,696,698,699,700,702,701,704,703,705,706,707,709,708,711,710,713,712,715,714,716,718,717,719,721,720,722,724,723,725,726,728,727,729,730,732,731,734,733,736,735,737,739,738,741,740,743,742,744,746,745,748,747,750,749,751,753,752,754,755,757,756,759,758,761,760,762,764,763,765,766,768,767,770,769,771,773,772,775,774,776,777,779,778,781,780,783,782,785,784,786,788,787,789,791,790,792,793,795,794,796,798,797,800,799,801,802,803,805,804,806,807,809,808,811,810,812,813,814,816,815,818,817,819,821,820,822,823,824,825,826,828,827,829,830,832,831,833,834,835,836,837,838,839,841,840,843,842,844,845,846,847,849,848,851,850,852,853,854,855,857,856,858,859,861,860,863,862,865,864,866,868,867,870,869,872,871,874,873,876,875,877,879,878,880,882,881,884,883,885,887,886,888,889,891,890,893,892,895,894,896,898,897,899,901,900,902,904,903,905,907,906,908,910,909,911,912,913,915,914,916,917,919,918,921,920,923,922,925,924,926,928,927,930,929,931,932,934,933,935,937,936,939,938,940,941,943,942,944,945,947,946,949,948,950,952,951,954,953,956,955,957,959,958,960,961,962,964,963,965,967,966,968,969,971,970,972,974,973,975,977,976,978,979,980,982,981,983,984,985,986,987,989,988,991,990,992,993,995,994,997,996,999,998,1000,1001,1002,1004,1003,1005,1007,1006,1008,1010,1009,1011,1012,1013,1015,1014,1016,1018,1017,1019,1021,1020,1022,1024,1023,1026,1025,1027,1028,1030,1029,1032,1031,1033,1034,1035,1037,1036,1039,1038,1041,1040,1042,1044,1043,1045,1047,1046,1049,1048,1051,1050,1052,1054,1053,1056,1055,1057,1059,1058,1060,1061,1063,1062,1065,1064,1067,1066,1069,1068,1070,1071,1072,1073,1074,1075,1077,1076,1078,1080,1079,1082,1081,1083,1084,1085,1087,1086,1088,1089,1090,1092,1091,1094,1093,1096,1095,1098,1097,1100,1099,1101,1102,1103,1104,1106,1105,1108,1107,1109,1110,1111,1112,1113,1115,1114,1117,1116,1118,1120,1119,1121,1122,1123,1125,1124,1127,1126,1129,1128,1131,1130,1132,1133,1135,1134,1136,1138,1137,1139,1141,1140,1143,1142,1145,1144,1146,1148,1147,1149,1150,1151,1153,1152,1155,1154,1157,1156,1158,1159,1161,1160,1163,1162,1165,1164,1167,1166,1168,1169,1170,1171,1172,1174,1173,1176,1175,1177,1178,1180,1179,1182,1181,1184,1183,1186,1185,1187,1188,1189,1191,1190,1193,1192,1195,1194,1197,1196,1199,1198,1201,1200,1203,1202,1205,1204,1206,1208,1207,1209,1211,1210,1213,1212,1215,1214,1216,1217,1219,1218,1221,1220,1222,1224,1223,1225,1226,1228,1227,1230,1229,1231,1232,1233,1235,1234,1236,1238,1237,1239,1241,1240,1243,1242,1245,1244,1246,1247,1248,1249,1250,1252,1251,1254,1253,1256,1255,1257,1258,1259,1261,1260,1263,1262,1265,1264,1266,1268,1267,1270,1269,1271,1273,1272,1275,1274,1276,1277,1279,1278,1281,1280,1283,1282,1285,1284,1287,1286,1288,1289,1290,1292,1291,1293,1294,1295,1297,1296,1299,1298,1300,1302,1301,1303,1305,1304,1307,1306,1309,1308,1310,1312,1311,1313,1314,1316,1315,1317,1318,1319,1320,1321,1322,1323,1324,1325,1326,1328,1327,1330,1329,1331,1332,1333,1334,1336,1335,1337,1338,1340,1339,1341,1343,1342,1345,1344,1346,1347,1349,1348,1350,1351,1353,1352,1354,1356,1355,1358,1357,1360,1359,1362,1361,1363,1364,1366,1365,1367,1369,1368,1370,1372,1371,1373,1374,1376,1375,1377,1379,1378,1380,1382,1381,1383,1385,1384,1386,1387,1389,1388,1390,1391,1392,1393,1394,1395,1397,1396,1398,1399,1401,1400,1403,1402,1405,1404,1407,1406,1408,1410,1409,1411,1412,1413,1415,1414,1417,1416,1418,1420,1419,1421,1423,1422,1425,1424,1426,1428,1427,1430,1429,1432,1431,1434,1433,1436,1435,1438,1437,1440,1439,1441,1442,1443,1444,1445,1447,1446,1449,1448,1450,1451,1452,1453,1455,1454,1457,1456,1458,1460,1459,1462,1461,1464,1463,1465,1466,1468,1467,1469,1470,1472,1471,1474,1473,1475,1476,1478,1477,1479,1481,1480,1482,1484,1483,1485,1486,1487,1488,1490,1489,1492,1491,1494,1493,1495,1497,1496,1498,1500,1499,1502,1501,1503,1504,1506,1505,1507,1509,1508,1511,1510,1513,1512,1515,1514,1516,1517,1518,1520,1519,1521,1522,1523,1524,1525,1526,1527,1529,1528,1531,1530,1533,1532,1535,1534,1537,1536,1539,1538,1541,1540,1543,1542,1544,1546,1545,1548,1547,1549,1551,1550,1552,1554,1553,1555,1557,1556,1559,1558,1560,1561,1562,1564,1563,1565,1566,1568,1567,1569,1570,1572,1571,1573,1575,1574,1577,1576,1578,1580,1579,1581,1583,1582,1585,1584,1586,1588,1587,1590,1589,1592,1591,1594,1593,1596,1595,1597,1598,1599,1600,1601,1602,1603,1605,1604,1607,1606,1608,1609,1610,1612,1611,1613,1614,1616,1615,1617,1619,1618,1621,1620,1623,1622,1624,1626,1625,1628,1627,1629,1631,1630,1632,1633,1635,1634,1636,1637,1638,1639,1640,1642,1641,1644,1643,1645,1647,1646,1649,1648,1651,1650,1653,1652,1654,1655,1656,1657,1659,1658,1661,1660,1663,1662,1665,1664,1667,1666,1669,1668,1670,1672,1671,1674,1673,1676,1675,1677,1679,1678,1680,1681,1683,1682,1685,1684,1687,1686,1688,1690,1689,1692,1691,1694,1693,1695,1697,1696,1698,1700,1699,1701,1703,1702,1704,1705,1707,1706,1708,1709,1711,1710,1712,1713,1714,1715,1717,1716,1719,1718,1720,1721,1722,1724,1723,1726,1725,1727,1729,1728,1731,1730,1733,1732,1734,1736,1735,1738,1737,1740,1739,1741,1742,1744,1743,1745,1746,1748,1747,1750,1749,1752,1751,1754,1753,1755,1756,1757,1758,1759,1760,1762,1761,1764,1763,1766,1765,1767,1769,1768,1771,1770,1773,1772,1775,1774,1777,1776,1778,1780,1779,1782,1781,1783,1785,1784,1787,1786,1789,1788,1790,1791,1793,1792,1794,1795,1796,1797,1799,1798,1801,1800,1802,1804,1803,1806,1805,1807,1808,1810,1809,1811,1813,1812,1815,1814,1816,1818,1817,1819,1821,1820,1822,1824,1823,1825,1827,1826,1829,1828,1831,1830,1833,1832,1835,1834,1837,1836,1838,1840,1839,1842,1841,1843,1844,1846,1845,1848,1847,1850,1849,1851,1853,1852,1855,1854,1857,1856,1859,1858,1860,1862,1861,1864,1863,1865,1866,1867,1868,1870,1869,1872,1871,1874,1873,1875,1877,1876,1878,1880,1879,1882,1881,1883,1884,1886,1885,1887,1888,1890,1889,1891,1892,1894,1893,1896,1895,1898,1897,1900,1899,1901,1902,1903,1905,1904,1907,1906,1908,1909,1910,1912,1911,1914,1913,1915,1916,1918,1917,1919,1921,1920,1923,1922,1925,1924,1926,1927,1928,1930,1929,1932,1931,1934,1933,1936,1935,1938,1937,1940,1939,1941,1943,1942,1944,1946,1945,1948,1947,1950,1949,1952,1951,1953,1954,1955,1957,1956,1958,1959,1961,1960,1962,1964,1963,1965,1966,1968,1967,1970,1969,1971,1972,1973,1975,1974,1976,1977,1979,1978,1981,1980,1983,1982,1985,1984,1987,1986,1988,1990,1989,1991,1993,1992,1994,1995,1997,1996,1999,1998,2000,2001,2003,2002,2004,2005,2007,2006,2008,2009,2011,2010,2012,2013,2014,2016,2015,2017,2019,2018,2020,2022,2021,2024,2023,2025,2026,2027,2029,2028,2030,2032,2031,2033,2034,2035,2036,2037,2038,2039,2041,2040,2043,2042,2045,2044,2046,2047,2048,2050,2049,2051,2052,2054,2053,2055,2057,2056,2058,2059,2060,2062,2061,2063,2064,2066,2065,2067,2068,2069,2070,2071,2073,2072,2075,2074,2076,2077,2079,2078,2080,2081,2083,2082,2084,2086,2085,2088,2087,2089,2091,2090,2093,2092,2095,2094,2097,2096,2099,2098,2100,2102,2101,2104,2103,2105,2107,2106,2109,2108,2110,2112,2111,2113,2114,2115,2117,2116,2119,2118,2121,2120,2122,2124,2123,2125,2127,2126,2129,2128,2130,2131,2133,2132,2135,2134,2137,2136,2139,2138,2141,2140,2143,2142,2145,2144,2147,2146,2148,2150,2149,2151,2152,2154,2153,2155,2157,2156,2158,2160,2159,2162,2161,2164,2163,2165,2167,2166,2168,2170,2169,2171,2172,2174,2173,2175,2176,2177,2178,2179,2181,2180,2183,2182,2185,2184,2186,2188,2187,2190,2189,2192,2191,2193,2195,2194,2196,2197,2199,2198,2201,2200,2203,2202,2205,2204,2207,2206,2209,2208,2211,2210,2212,2213,2214,2216,2215,2218,2217,2219,2221,2220,2223,2222,2224,2225,2226,2227,2229,2228,2230,2232,2231,2233,2235,2234,2236,2238,2237,2239,2240,2241,2242,2243,2244,2245,2246,2247,2248,2249,2251,2250,2252,2254,2253,2256,2255,2258,2257,2259,2261,2260,2263,2262,2264,2265,2266,2268,2267,2270,2269,2271,2273,2272,2275,2274,2277,2276,2279,2278,2281,2280,2282,2284,2283,2285,2286,2288,2287,2290,2289,2292,2291,2293,2294,2295,2296,2297,2298,2300,2299,2301,2303,2302,2305,2304,2306,2307,2309,2308,2310,2311,2313,2312,2314,2316,2315,2318,2317,2320,2319,2322,2321,2324,2323,2325,2327,2326,2329,2328,2330,2332,2331,2334,2333,2336,2335,2338,2337,2339,2341,2340,2343,2342,2345,2344,2347,2346,2348,2350,2349,2351,2353,2352,2355,2354,2356,2357,2358,2359,2360,2362,2361,2363,2365,2364,2366,2368,2367,2370,2369,2372,2371,2373,2375,2374,2376,2377,2378,2380,2379,2381,2383,2382,2385,2384,2386,2388,2387,2390,2389,2391,2392,2393,2395,2394,2397,2396,2399,2398,2400,2402,2401,2403,2404,2405,2407,2406,2408,2409,2411,2410,2413,2412,2415,2414,2417,2416,2419,2418,2421,2420,2423,2422,2425,2424,2427,2426,2428,2430,2429,2431,2433,2432,2435,2434,2437,2436,2439,2438,2440,2441,2443,2442,2444,2446,2445,2448,2447,2450,2449,2451,2452,2453,2454,2455,2457,2456,2459,2458,2461,2460,2462,2464,2463,2465,2466,2467,2468,2470,2469,2471,2473,2472,2475,2474,2477,2476,2479,2478,2480,2481,2483,2482,2484,2486,2485,2487,2488,2489,2491,2490,2493,2492,2495,2494,2497,2496,2499,2498,2500,2501,2502,2503,2505,2504,2507,2506,2509,2508,2510,2511,2512,2514,2513,2515,2516,2517,2519,2518,2520,2522,2521,2524,2523,2525,2526,2527,2529,2528,2530,2532,2531,2534,2533,2536,2535,2537,2539,2538,2541,2540,2542,2543,2544,2546,2545,2548,2547,2549,2551,2550,2553,2552,2555,2554,2556,2557,2559,2558,2561,2560,2563,2562,2564,2566,2565,2567,2569,2568,2571,2570,2572,2574,2573,2576,2575,2578,2577,2579,2580,2581,2583,2582,2585,2584,2587,2586,2588,2589,2591,2590,2592,2593,2595,2594,2596,2598,2597,2599,2600,2601,2603,2602,2604,2605,2607,2606,2609,2608,2611,2610,2612,2614,2613,2616,2615,2618,2617,2620,2619,2622,2621,2624,2623,2625,2626,2628,2627,2630,2629,2631,2633,2632,2635,2634,2637,2636,2639,2638,2641,2640,2642,2644,2643,2645,2647,2646,2648,2650,2649,2652,2651,2653,2655,2654,2656,2657,2659,2658,2660,2662,2661,2664,2663,2665,2667,2666,2669,2668,2670,2671,2672,2674,2673,2675,2677,2676,2678,2679,2680,2681,2683,2682,2685,2684,2686,2687,2689,2688,2691,2690,2693,2692,2695,2694,2697,2696,2698,2700,2699,2701,2703,2702,2705,2704,2707,2706,2708,2709,2711,2710,2713,2712,2714,2715,2717,2716,2718,2720,2719,2721,2723,2722,2725,2724,2726,2728,2727,2730,2729,2731,2733,2732,2734,2736,2735,2737,2739,2738,2740,2741,2742,2744,2743,2746,2745,2748,2747,2750,2749,2752,2751,2754,2753,2755,2756,2758,2757,2760,2759,2762,2761,2764,2763,2766,2765,2768,2767,2770,2769,2772,2771,2774,2773,2775,2777,2776,2778,2779,2781,2780,2782,2784,2783,2785,2787,2786,2789,2788,2790,2791,2792,2794,2793,2796,2795,2797,2799,2798,2800,2801,2803,2802,2804,2806,2805,2808,2807,2810,2809,2811,2813,2812,2815,2814,2817,2816,2818,2819,2821,2820,2823,2822,2824,2826,2825,2828,2827,2830,2829,2831,2833,2832,2834,2836,2835,2838,2837,2840,2839,2841,2842,2844,2843,2846,2845,2847,2849,2848,2851,2850,2853,2852,2854,2855,2857,2856,2859,2858,2860,2862,2861,2864,2863,2865,2867,2866,2868,2870,2869,2871,2872,2874,2873,2875,2876,2878,2877,2880,2879,2882,2881,2883,2885,2884,2886,2887,2888,2889,2890,2891,2893,2892,2894,2896,2895,2897,2899,2898,2901,2900,2903,2902,2904,2905,2907,2906,2909,2908,2910,2912,2911,2914,2913,2915,2917,2916,2919,2918,2920,2922,2921,2924,2923,2926,2925,2928,2927,2929,2931,2930,2933,2932,2935,2934,2937,2936,2939,2938,2940,2941,2942,2944,2943,2945,2946,2947,2949,2948,2951,2950,2953,2952,2955,2954,2956,2958,2957,2960,2959,2961,2962,2964,2963,2966,2965,2968,2967,2969,2971,2970,2972,2973,2975,2974,2976,2977,2979,2978,2980,2982,2981,2984,2983,2986,2985,2987,2989,2988,2990,2991,2993,2992,2994,2996,2995,2998,2997,2999,3000,3002,3001,3004,3003,3005,3007,3006,3008,3009,3010,3011,3013,3012,3014,3015,3017,3016,3019,3018,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3032,3031,3033,3035,3034,3036,3037,3038,3039,3040,3042,3041,3043,3044,3046,3045,3048,3047,3050,3049,3052,3051,3054,3053,3055,3057,3056,3058,3059,3061,3060,3063,3062,3064,3066,3065,3067,3069,3068,3071,3070,3072,3073,3075,3074,3076,3077,3078,3079,3081,3080,3082,3084,3083,3085,3087,3086,3089,3088,3090,3091,3093,3092,3095,3094,3097,3096,3099,3098,3100,3101,3102,3103,3105,3104,3107,3106,3109,3108,3110,3112,3111,3114,3113,3115,3116,3118,3117,3119,3121,3120,3122,3124,3123,3125,3126,3128,3127,3129,3130,3131,3133,3132,3134,3136,3135,3137,3139,3138,3141,3140,3142,3143,3144,3146,3145,3147,3148,3149,3150,3151,3153,3152,3154,3155,3156,3158,3157,3160,3159,3161,3162,3163,3164,3166,3165,3168,3167,3169,3171,3170,3173,3172,3174,3175,3177,3176,3179,3178,3180,3182,3181,3183,3184,3186,3185,3188,3187,3189,3191,3190,3192,3193,3194,3196,3195,3198,3197,3199,3200,3201,3203,3202,3205,3204,3206,3208,3207,3210,3209,3212,3211,3213,3214,3215,3216,3217,3218,3220,3219,3222,3221,3223,3225,3224,3227,3226,3229,3228,3231,3230,3232,3234,3233,3236,3235,3237,3239,3238,3240,3241,3243,3242,3244,3246,3245,3247,3248,3250,3249,3251,3252,3254,3253,3256,3255,3257,3259,3258,3260,3262,3261,3263,3265,3264,3266,3267,3269,3268,3270,3271,3273,3272,3274,3276,3275,3277,3279,3278,3280,3282,3281,3284,3283,3286,3285,3287,3288,3289,3291,3290,3293,3292,3294,3296,3295,3298,3297,3299,3300,3301,3302,3303,3304,3305,3307,3306,3309,3308,3310,3312,3311,3314,3313,3316,3315,3317,3319,3318,3321,3320,3323,3322,3324,3326,3325,3327,3329,3328,3331,3330,3333,3332,3334,3336,3335,3337,3338,3339,3340,3342,3341,3343,3344,3346,3345,3347,3348,3349,3351,3350,3352,3354,3353,3356,3355,3358,3357,3359,3361,3360,3363,3362,3365,3364,3367,3366,3369,3368,3370,3372,3371,3373,3374,3376,3375,3377,3378,3379,3380,3382,3381,3383,3384,3385,3386,3388,3387,3389,3390,3391,3392,3394,3393,3395,3396,3397,3398,3399,3401,3400,3403,3402,3405,3404,3406,3408,3407,3410,3409,3411,3413,3412,3414,3415,3417,3416,3418,3419,3421,3420,3423,3422,3424,3426,3425,3428,3427,3429,3431,3430,3432,3433,3435,3434,3437,3436,3439,3438,3440,3441,3442,3443,3445,3444,3447,3446,3449,3448,3450,3452,3451,3453,3454,3456,3455,3458,3457,3459,3461,3460,3463,3462,3464,3466,3465,3467,3468,3470,3469,3471,3472,3474,3473,3476,3475,3478,3477,3479,3480,3481,3483,3482,3485,3484,3486,3488,3487,3489,3490,3492,3491,3494,3493,3495,3496,3498,3497,3499,3500,3501,3502,3503,3504,3505,3507,3506,3508,3509,3510,3512,3511,3514,3513,3516,3515,3518,3517,3519,3520,3522,3521,3523,3525,3524,3527,3526,3528,3530,3529,3532,3531,3534,3533,3535,3537,3536,3539,3538,3541,3540,3542,3544,3543,3546,3545,3548,3547,3549,3551,3550,3553,3552,3555,3554,3556,3557,3559,3558,3560,3561,3563,3562,3564,3566,3565,3567,3568,3570,3569,3572,3571,3574,3573,3575,3577,3576,3578,3580,3579,3581,3582,3583,3585,3584,3586,3587,3588,3589,3590,3592,3591,3593,3595,3594,3596,3597,3599,3598,3601,3600,3603,3602,3604,3606,3605,3608,3607,3609,3610,3612,3611,3614,3613,3616,3615,3618,3617,3619,3620,3621,3622,3623,3625,3624,3627,3626,3628,3629,3631,3630,3632,3634,3633,3636,3635,3638,3637,3639,3641,3640,3643,3642,3645,3644,3646,3648,3647,3650,3649,3652,3651,3654,3653,3656,3655,3657,3658,3659,3661,3660,3662,3664,3663,3666,3665,3668,3667,3669,3671,3670,3673,3672,3674,3676,3675,3677,3679,3678,3680,3682,3681,3683,3684,3686,3685,3688,3687,3689,3691,3690,3692,3694,3693,3696,3695,3697,3698,3700,3699,3701,3702,3704,3703,3706,3705,3707,3708,3710,3709,3712,3711,3714,3713,3715,3717,3716,3719,3718,3720,3722,3721,3723,3725,3724,3727,3726,3728,3729,3731,3730,3733,3732,3734,3735,3736,3738,3737,3739,3740,3741,3742,3743,3745,3744,3746,3748,3747,3750,3749,3751,3753,3752,3755,3754,3756,3757,3759,3758,3760,3762,3761,3764,3763,3765,3767,3766,3769,3768,3770,3771,3773,3772,3774,3776,3775,3777,3779,3778,3780,3781,3782,3783,3785,3784,3787,3786,3788,3789,3791,3790,3792,3794,3793,3795,3797,3796,3799,3798,3800,3802,3801,3803,3804,3805,3806,3808,3807,3810,3809,3811,3812,3813,3814,3816,3815,3817,3818,3819,3820,3822,3821,3824,3823,3825,3827,3826,3828,3829,3830,3832,3831,3834,3833,3836,3835,3838,3837,3840,3839,3842,3841,3843,3844,3845,3847,3846,3849,3848,3850,3851,3852,3854,3853,3856,3855,3858,3857,3860,3859,3861,3863,3862,3864,3866,3865,3867,3869,3868,3871,3870,3873,3872,3875,3874,3876,3877,3878,3880,3879,3881,3883,3882,3884,3886,3885,3888,3887,3889,3890,3892,3891,3894,3893,3895,3896,3897,3899,3898,3901,3900,3903,3902,3905,3904,3906,3907,3908,3910,3909,3912,3911,3913,3914,3915,3916,3917,3918,3920,3919,3922,3921,3923,3924,3925,3926,3928,3927,3930,3929,3931,3933,3932,3935,3934,3937,3936,3939,3938,3941,3940,3943,3942,3944,3945,3946,3947,3949,3948,3950,3952,3951,3953,3955,3954,3957,3956,3958,3959,3960,3962,3961,3964,3963,3965,3966,3967,3969,3968,3970,3972,3971,3973,3975,3974,3977,3976,3978,3980,3979,3982,3981,3984,3983,3986,3985,3988,3987,3990,3989,3992,3991,3994,3993,3996,3995,3998,3997,4000,3999,4001,4002,4003,4005,4004,4007,4006,4009,4008,4010,4011,4013,4012,4015,4014,4017,4016,4018,4019,4020,4022,4021,4023,4025,4024,4027,4026,4029,4028,4031,4030,4033,4032,4035,4034,4037,4036,4038,4040,4039,4042,4041,4043,4044,4045,4046,4048,4047,4049,4051,4050,4053,4052,4054,4056,4055,4058,4057,4059,4061,4060,4063,4062,4064,4065,4066,4067,4068,4069,4070,4072,4071,4074,4073,4076,4075,4078,4077,4079,4081,4080,4083,4082,4085,4084,4087,4086,4088,4090,4089,4091,4092,4094,4093,4095,4097,4096,4099,4098,4100,4102,4101,4103,4105,4104,4106,4107,4108,4110,4109,4112,4111,4113,4114,4115,4116,4117,4118,4120,4119,4121,4123,4122,4125,4124,4126,4128,4127,4130,4129,4131,4132,4133,4134,4135,4136,4138,4137,4139,4141,4140,4143,4142,4145,4144,4147,4146,4148,4149,4151,4150,4153,4152,4154,4156,4155,4158,4157,4159,4160,4161,4163,4162,4165,4164,4166,4168,4167,4170,4169,4172,4171,4174,4173,4176,4175,4177,4179,4178,4180,4182,4181,4183,4185,4184,4187,4186,4189,4188,4190,4192,4191,4194,4193,4196,4195,4198,4197,4199,4200,4201,4202,4203,4205,4204,4207,4206,4208,4210,4209,4212,4211,4213,4215,4214,4217,4216,4219,4218,4221,4220,4222,4224,4223,4226,4225,4227,4228,4229,4230,4231,4233,4232,4235,4234,4236,4237,4239,4238,4240,4242,4241,4244,4243,4246,4245,4248,4247,4249,4251,4250,4253,4252,4254,4255,4256,4257,4258,4260,4259,4262,4261,4264,4263,4265,4267,4266,4269,4268,4271,4270,4273,4272,4275,4274,4276,4277,4278,4280,4279,4281,4283,4282,4284,4286,4285,4287,4288,4289,4291,4290,4292,4293,4294,4295,4296,4298,4297,4300,4299,4302,4301,4303,4305,4304,4306,4308,4307,4309,4310,4311,4313,4312,4314,4316,4315,4318,4317,4319,4321,4320,4323,4322,4325,4324,4326,4327,4328,4329,4331,4330,4333,4332,4334,4336,4335,4337,4339,4338,4340,4342,4341,4344,4343,4346,4345,4348,4347,4350,4349,4352,4351,4353,4354,4356,4355,4358,4357,4359,4361,4360,4363,4362,4364,4366,4365,4368,4367,4369,4371,4370,4373,4372,4374,4375,4376,4378,4377,4380,4379,4382,4381,4383,4384,4385,4386,4388,4387,4389,4390,4391,4393,4392,4394,4396,4395,4397,4398,4399,4401,4400,4402,4404,4403,4406,4405,4407,4409,4408,4410,4411,4412,4413,4415,4414,4416,4417,4419,4418,4420,4422,4421,4423,4424,4425,4427,4426,4428,4429,4430,4431,4432,4434,4433,4435,4436,4438,4437,4440,4439,4441,4443,4442,4444,4446,4445,4448,4447,4450,4449,4451,4452,4454,4453,4455,4457,4456,4458,4460,4459,4462,4461,4464,4463,4465,4466,4467,4469,4468,4470,4472,4471,4474,4473,4475,4477,4476,4479,4478,4481,4480,4482,4483,4484,4485,4486,4487,4488,4490,4489,4491,4493,4492,4495,4494,4496,4498,4497,4500,4499,4501,4502,4504,4503,4505,4507,4506,4509,4508,4511,4510,4513,4512,4514,4516,4515,4517,4519,4518,4520,4521,4522,4523,4524,4526,4525,4527,4528,4529,4531,4530,4533,4532,4534,4535,4537,4536,4539,4538,4540,4541,4542,4544,4543,4545,4546,4548,4547,4550,4549,4552,4551,4553,4554,4555,4557,4556,4559,4558,4561,4560,4562,4564,4563,4565,4566,4568,4567,4569,4570,4571,4573,4572,4574,4575,4577,4576,4578,4579,4581,4580,4582,4583,4585,4584,4587,4586,4589,4588,4590,4591,4592,4594,4593,4595,4597,4596,4599,4598,4600,4602,4601,4603,4605,4604,4606,4607,4609,4608,4610,4611,4612,4613,4614,4616,4615,4617,4619,4618,4620,4621,4623,4622,4625,4624,4627,4626,4628,4629,4631,4630,4633,4632,4634,4635,4636,4637,4638,4640,4639,4642,4641,4644,4643,4645,4646,4648,4647,4649,4650,4651,4653,4652,4655,4654,4657,4656,4659,4658,4660,4661,4663,4662,4665,4664,4666,4667,4668,4669,4670,4672,4671,4674,4673,4676,4675,4677,4678,4680,4679,4681,4682,4683,4685,4684,4687,4686,4688,4690,4689,4692,4691,4693,4695,4694,4696,4698,4697,4699,4701,4700,4703,4702,4704,4706,4705,4707,4708,4710,4709,4712,4711,4713,4715,4714,4717,4716,4719,4718,4721,4720,4722,4724,4723,4726,4725,4727,4728,4729,4730,4731,4732,4733,4735,4734,4737,4736,4739,4738,4741,4740,4743,4742,4745,4744,4747,4746,4749,4748,4750,4751,4753,4752,4755,4754,4756,4757,4758,4759,4761,4760,4762,4763,4764,4766,4765,4768,4767,4769,4770,4772,4771,4774,4773,4776,4775,4778,4777,4779,4781,4780,4783,4782,4784,4785,4787,4786,4789,4788,4790,4791,4793,4792,4795,4794,4797,4796,4799,4798,4801,4800,4803,4802,4804,4805,4807,4806,4808,4809,4811,4810,4813,4812,4814,4816,4815,4818,4817,4820,4819,4822,4821,4823,4825,4824,4827,4826,4829,4828,4831,4830,4833,4832,4835,4834,4836,4837,4838,4839,4841,4840,4842,4844,4843,4846,4845,4848,4847,4850,4849,4851,4852,4854,4853,4856,4855,4857,4858,4859,4860,4861,4863,4862,4865,4864,4866,4867,4868,4869,4870,4871,4872,4873,4874,4876,4875,4878,4877,4879,4881,4880,4882,4883,4885,4884,4886,4887,4888,4890,4889,4892,4891,4893,4894,4896,4895,4898,4897,4899,4900,4901,4903,4902,4905,4904,4906,4908,4907,4910,4909,4912,4911,4914,4913,4916,4915,4918,4917,4919,4920,4921,4922,4924,4923,4925,4926,4928,4927,4930,4929,4931,4933,4932,4934,4936,4935,4938,4937,4940,4939,4941,4943,4942,4945,4944,4946,4948,4947,4950,4949,4952,4951,4954,4953,4956,4955,4957,4959,4958,4961,4960,4962,4963,4965,4964,4967,4966,4969,4968,4970,4971,4973,4972,4974,4975,4976,4977,4978,4980,4979,4981,4983,4982,4984,4986,4985,4988,4987,4990,4989,4992,4991,4993,4995,4994,4996,4998,4997,4999]
# A = [2,0,1]
solution = Solution()
print(solution.isIdealPermutation(A))
