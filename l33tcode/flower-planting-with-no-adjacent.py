class Solution:
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        result = [1] * N
        adj = [set() for _ in range(N)]

        for edge in paths:
            begin, end = edge[0] - 1, edge[1] - 1
            adj[begin].add(end)
            adj[end].add(begin)
            if result[end] == result[begin]:
                avail = set([1, 2, 3, 4])
                for garden in adj[end]:
                    avail.discard(result[garden])
                result[end] = avail.pop()

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.gardenNoAdj(0, []) == []

    def test_custom1(self):
        assert self.sol.gardenNoAdj(3, [[1,2],[2,3],[3,1]]) == [3, 2, 1]

    def test_custom2(self):
        assert self.sol.gardenNoAdj(4, [[1,2],[3,4]]) == [1, 2, 1, 2]

    def test_custom3(self):
        assert self.sol.gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]) == [1, 2, 3, 4]

    def test_custom4(self):
        assert self.sol.gardenNoAdj(5, [[1,2],[3,4],[4,1],[1,3],[2,4],[5,2]]) == [1, 2, 3, 4, 1]

    def test_custom5(self):
        assert self.sol.gardenNoAdj(3000, [[667,1340],[1117,2534],[1014,2122],[2114,407],[2722,603],[2678,2020],[934,1138],[2187,1724],[2038,2656],[1456,1010],[930,2065],[186,558],[1406,770],[2564,1642],[1768,2753],[1599,622],[2359,1182],[1940,2087],[2501,1692],[2894,868],[1327,501],[184,1090],[754,2293],[599,1072],[721,1137],[1846,2627],[128,1967],[1302,1523],[2267,1350],[677,2646],[1723,1949],[2409,1654],[937,899],[2794,562],[1253,1054],[645,1534],[2222,2987],[1320,2276],[1455,2397],[1069,2349],[55,1504],[1382,74],[1047,304],[1114,1601],[1773,540],[46,1162],[2913,2193],[1852,1314],[1527,2747],[1101,656],[2253,2759],[2079,2192],[2794,1489],[979,2257],[1908,266],[1013,2617],[2327,182],[1213,1059],[815,772],[1686,2178],[693,2604],[1869,904],[291,104],[196,1021],[1006,1585],[2923,2626],[1769,175],[140,1089],[1211,2708],[942,2012],[969,1745],[1190,1586],[1177,2201],[1585,1319],[347,2553],[849,1800],[1383,1200],[774,1466],[1653,407],[809,2080],[527,552],[1147,356],[2509,488],[2212,2978],[438,993],[986,1313],[202,1853],[2223,2920],[1262,1986],[1308,504],[835,2656],[159,2612],[2273,1562],[2762,1597],[1539,666],[1399,2456],[49,1310],[2121,2000],[11,1483],[1452,785],[2492,2986],[1275,1730],[10,1665],[1626,2492],[823,313],[200,2781],[1393,2266],[2004,1485],[2886,1028],[314,1284],[2940,2131],[1383,1439],[166,1461],[292,1131],[490,94],[2467,1548],[1321,2002],[807,2794],[2883,2387],[204,2272],[1839,1849],[966,341],[1974,2705],[426,1367],[2463,1366],[1976,2176],[338,1470],[2632,2955],[2711,1416],[904,2714],[1188,467],[1631,2602],[1291,610],[899,916],[1896,1104],[390,1411],[1514,34],[453,2693],[325,1859],[1423,1214],[2201,2022],[383,1152],[2829,2009],[1938,2558],[1067,296],[1998,1141],[1593,2138],[2960,962],[1809,288],[2342,368],[2910,2664],[944,1913],[1290,2870],[2916,1735],[2083,655],[259,1717],[667,2810],[1161,914],[1741,2256],[682,598],[208,1925],[2065,2745],[1996,2070],[832,463],[820,2090],[2948,564],[804,1217],[2505,2191],[468,2073],[2336,1044],[2304,444],[1483,927],[2672,193],[680,995],[1541,1826],[1662,2345],[1498,1985],[2191,1178],[1152,1459],[796,1468],[982,955],[902,2705],[1828,1817],[1778,846],[1097,2223],[2246,63],[73,2679],[1444,133],[622,2159],[592,1631],[2041,682],[2653,2021],[2527,965],[2720,1509],[2730,746],[2504,2253],[1437,803],[1040,1282],[1845,2647],[1556,1359],[921,2107],[102,1144],[2053,186],[895,2419],[1402,631],[2697,2406],[2365,228],[1530,2132],[1564,2364],[2139,2523],[736,1425],[1848,1649],[739,931],[2649,2393],[430,1016],[1154,2997],[135,2518],[509,112],[1019,1440],[127,657],[366,2817],[921,2721],[2770,2293],[2909,1069],[1253,1353],[2027,2924],[2949,281],[1298,929],[2000,2978],[1384,2068],[316,559],[536,323],[2406,1787],[1873,554],[2885,645],[1890,2074],[12,1690],[1974,194],[20,2901],[1452,1973],[1737,638],[2660,2348],[1605,75],[2558,667],[1651,2200],[619,967],[1550,974],[2285,1938],[1722,1429],[2068,2858],[1517,808],[301,188],[1021,2463],[1893,2322],[506,651],[2444,258],[1094,2291],[704,1674],[983,759],[34,338],[1199,221],[2770,2354],[1961,890],[2497,123],[2530,2198],[2025,1193],[774,671],[1966,2295],[590,2714],[828,463],[1829,1589],[2625,2099],[2153,2914],[2697,1172],[1204,1395],[2379,484],[1398,2943],[2906,2117],[2201,2568],[2275,1902],[954,2873],[1261,331],[1804,2992],[1213,770],[212,122],[117,1695],[238,2198],[1394,2865],[712,490],[1297,1138],[1952,2601],[430,2326],[188,937],[792,1622],[1194,1157],[204,1242],[2985,2268],[2132,130],[71,2564],[724,1449],[2867,1391],[1515,1430],[1836,2221],[2934,2148],[2488,2798],[646,441],[1659,169],[1313,1969],[919,1690],[1812,2002],[358,2394],[1254,300],[1644,1922],[878,310],[1835,1137],[829,1608],[2465,433],[2627,25],[2903,906],[103,773],[2335,627],[2469,1517],[2305,714],[1788,1009],[1726,1444],[382,526],[1645,724],[2776,1597],[2021,1377],[1578,1345],[363,1280],[483,564],[1039,762],[777,2034],[1089,2654],[150,323],[326,902],[180,2646],[728,105],[2507,2962],[1477,2326],[615,2725],[2190,2379],[2600,402],[311,1346],[1363,2586],[1142,2988],[1017,2897],[2549,868],[1040,585],[980,1097],[2511,297],[92,878],[838,2457],[1233,2134],[1309,2208],[1086,530],[2301,883],[2190,1091],[1016,501],[230,2152],[2608,189],[660,991],[2398,809],[812,147],[1531,1287],[735,1556],[2393,2534],[2348,1623],[2333,990],[1466,2504],[745,1969],[2205,1065],[2954,503],[1638,404],[1097,1462],[2139,837],[2958,1111],[2200,2708],[2280,2742],[1282,2246],[1113,1727],[2876,2380],[678,2342],[77,985],[2994,2091],[1810,791],[2325,636],[2931,926],[1674,275],[92,2653],[871,1824],[2083,2553],[2068,2924],[1993,2989],[147,1383],[1334,1915],[2927,1592],[712,666],[669,825],[1359,2988],[1473,1865],[2301,315],[1662,613],[2082,170],[2975,1273],[674,641],[1505,1221],[1345,2093],[2351,725],[46,1625],[15,2445],[1417,2654],[2953,1171],[963,1694],[2421,1331],[424,863],[2447,472],[966,687],[825,2719],[2590,2824],[217,1740],[2401,2454],[1305,1451],[2676,1048],[2966,946],[2453,16],[933,586],[826,2979],[2211,482],[1195,2982],[168,1442],[2434,1447],[837,1985],[908,1567],[2872,204],[1830,157],[1718,2232],[622,6],[2615,2154],[2107,1486],[2720,1565],[2876,832],[2954,1397],[893,872],[674,1721],[376,784],[2511,1151],[2341,894],[2602,1144],[1764,1650],[1240,531],[842,2434],[1866,2959],[1041,528],[4,1754],[2886,1898],[2588,1316],[2394,2474],[1758,24],[1635,1937],[2439,475],[1348,378],[2850,2012],[2169,1829],[2649,230],[180,660],[2162,1354],[1518,2294],[1923,2097],[1294,2610],[325,1231],[2869,1732],[1141,2171],[1793,125],[2568,716],[2424,2641],[1970,2396],[1402,2975],[520,2478],[122,2179],[2469,2505],[2146,2513],[2577,794],[28,1240],[639,1003],[226,161],[2526,2319],[111,2276],[1336,2887],[287,2630],[1004,1963],[709,1300],[639,1312],[2792,1890],[682,1072],[1715,2216],[2235,1194],[1318,1992],[2345,2724],[108,684],[2036,1393],[298,1491],[1665,2391],[2827,461],[2454,2977],[306,445],[2337,2016],[2360,2374],[2194,1679],[946,1309],[210,2913],[2997,2422],[2913,2097],[1206,1279],[625,2386],[143,2684],[1402,1447],[2107,1682],[644,1596],[2897,72],[11,28],[119,963],[2977,573],[1486,2993],[2516,370],[2896,1736],[154,2951],[2678,2859],[864,1635],[2250,2475],[740,549],[2850,2357],[477,786],[192,1780],[1526,839],[764,2883],[254,1499],[1459,430],[651,2491],[11,2831],[2160,221],[2064,2112],[331,1188],[718,2701],[609,62],[2820,1074],[1283,963],[1757,576],[2309,865],[919,1453],[366,1752],[1207,1266],[477,1145],[413,1434],[828,286],[994,1628],[2998,1207],[2368,1074],[2237,1614],[922,230],[119,2478],[969,387],[2452,1702],[1421,1449],[124,1033],[2469,3],[2101,1490],[2715,2077],[184,196],[881,888],[1419,2718],[2842,2845],[2559,1789],[1080,2172],[564,988],[1772,1446],[1708,961],[160,2955],[401,36],[217,1959],[791,568],[1912,2792],[2047,1896],[98,294],[401,1380],[2188,851],[2690,1222],[247,1096],[1567,491],[1922,1584],[1503,1859],[2588,35],[35,1834],[268,1882],[2060,609],[2583,379],[1025,1543],[1624,342],[838,1319],[1506,1653],[184,1376],[2575,118],[323,2461],[2147,67],[522,498],[1008,1442],[2167,2936],[923,383],[540,427],[1882,1503],[1316,879],[782,2739],[2978,888],[1185,2876],[2133,2629],[2870,341],[1699,1253],[56,1719],[2986,38],[1777,1139],[1921,347],[975,2237],[1264,46],[2137,945],[2701,1853],[863,1682],[919,778],[1988,2436],[1586,1942],[270,1605],[2825,1572],[1866,301],[787,1744],[2084,490],[2421,1372],[1577,1092],[2095,883],[1311,2171],[1081,920],[697,225],[2540,2689],[2535,451],[29,2526],[1068,2646],[1842,2009],[1067,2105],[2702,2333],[969,1114],[1706,2045],[1815,511],[854,299],[2,2158],[1341,2775],[1013,844],[2,2900],[506,1311],[2289,2557],[2413,828],[72,2784],[2553,1908],[1597,1233],[1885,902],[1554,1363],[431,2146],[829,1358],[1779,2634],[460,2413],[1416,235],[2111,2377],[2175,2980],[2083,1226],[1847,1973],[1680,509],[2559,368],[1771,920],[906,129],[2460,2465],[55,2270],[1910,1719],[2472,395],[785,2395],[696,1993],[560,1835],[2274,349],[47,1530],[1439,1448],[2519,2859],[2766,1661],[1419,1367],[1965,822],[1585,1039],[1389,1624],[233,1419],[1429,2275],[1895,1757],[616,385],[928,191],[1069,660],[2131,1018],[1328,1687],[1412,322],[591,996],[1830,579],[2772,1235],[1718,2011],[2838,936],[955,180],[2374,2821],[1624,1883],[2769,2015],[78,1698],[709,1385],[2856,412],[2202,714],[2217,2314],[1824,1238],[1447,107],[358,1222],[2440,1831],[2310,760],[345,2450],[2357,2620],[350,2178],[2112,2309],[205,470],[102,183],[821,2304],[781,232],[234,740],[81,579],[2268,608],[1682,1463],[148,2760],[1531,915],[1255,2382],[1966,2641],[259,1916],[1734,1962],[1386,1422],[2583,2815],[2940,2463],[1594,1757],[922,558],[2213,1980],[1619,1852],[665,767],[1960,345],[2266,1169],[193,2540],[159,1158],[627,2165],[756,2313],[1869,2518],[2538,206],[1168,2895],[1770,1591],[1738,836],[2035,2186],[2662,2410],[1161,2170],[1296,2540],[606,2127],[318,643],[1745,429],[2774,121],[1787,1564],[1806,628],[783,41],[649,2282],[2983,2435],[1617,1171],[1098,2788],[2790,2548],[1887,1227],[1773,1119],[581,529],[85,2152],[1659,2279],[1504,753],[2868,1028],[2408,2492],[2633,2177],[2549,2473],[847,1912],[3000,710],[684,1939],[354,214],[1875,585],[2337,2106],[2460,2086],[212,961],[2252,694],[1918,668],[1703,2288],[2080,58],[1683,2398],[2593,1937],[2477,2951],[2159,2256],[2976,1648],[1046,2804],[2308,399],[49,2009],[1219,1485],[406,1294],[2335,703],[2165,316],[1674,2301],[2801,460],[2362,2604],[825,884],[2049,1261],[2297,1181],[960,2853],[1344,2192],[2547,140],[2186,8],[1900,1797],[1499,2330],[2719,2799],[2728,1988],[81,41],[1728,2747],[2644,1553],[1436,2288],[1892,79],[593,12],[1308,2444],[2206,870],[2826,2280],[1188,899],[2164,2021],[2748,861],[362,2380],[174,2938],[2795,606],[2834,1857],[1796,1241],[1406,173],[1818,1959],[894,2576],[1586,2910],[2055,1136],[2909,1029],[809,2331],[223,222],[690,370],[1706,2259],[1677,2805],[730,937],[645,521],[1242,1735],[1627,378],[2114,830],[865,1127],[1020,200],[1409,889],[1870,355],[2007,945],[2623,1160],[921,595],[502,777],[1773,2948],[2189,1025],[245,967],[798,718],[952,2828],[2548,1214],[1111,1223],[265,2969],[563,369],[2898,1233],[2498,2008],[2511,2105],[820,788],[1455,1791],[1547,1407],[2113,990],[2222,2018],[251,936],[1137,1895],[2152,92],[1235,379],[1536,196],[2727,1001],[2558,1307],[2542,1072],[301,1366],[527,2141],[2136,2974],[2282,852],[719,1529],[367,70],[2024,2402],[1126,753],[851,2334],[1297,2719],[2798,1499],[810,1180],[1711,2040],[856,2991],[2795,708],[559,1764],[327,1063],[1598,2071],[1935,1999],[1540,1014],[2154,2864],[2256,296],[1508,2230],[998,1154],[1957,2656],[2989,1286],[844,5],[2706,2672],[525,2655],[2703,2452],[2010,479],[758,1874],[1861,1276],[1972,917],[1047,2232],[1171,1713],[271,348],[2565,2300],[721,2079],[2313,1844],[1957,939],[873,2105],[2309,890],[596,537],[2909,53],[2225,226],[69,332],[330,127],[1413,1531],[2940,748],[2765,2910],[990,2527],[1353,901],[2192,2633],[36,2706],[2354,1814],[2421,1366],[966,1164],[2456,166],[1058,2264],[2181,1929],[871,1685],[771,613],[2183,1840],[968,857],[2839,942],[1013,2529],[153,54],[2995,1467],[1684,1337],[1080,172],[794,61],[273,129],[470,237],[282,44],[2544,753],[2501,2084],[854,950],[1691,793],[547,123],[2666,1508],[1422,1853],[563,2386],[818,2546],[1681,1918],[1410,366],[1649,769],[131,2742],[1730,703],[2692,1631],[1961,1793],[2510,518],[169,1295],[998,2362],[725,1724],[1946,2643],[2619,1575],[459,2284],[188,948],[2344,2963],[781,2681],[1205,2278],[2414,86],[2026,1673],[2930,2812],[140,1616],[1064,2920],[569,2130],[2087,2783],[1859,2209],[2799,1327],[1752,1311],[2707,2265],[2607,33],[367,1062],[2620,2944],[1321,2907],[785,2984],[1094,346],[2342,943],[1341,654],[1882,1280],[2833,1314],[144,757],[572,190],[1465,608],[1291,2168],[1831,2277],[2169,2488],[1998,938],[685,240],[1588,720],[2808,12],[1380,980],[106,2327],[1815,1660],[1780,276],[322,608],[1199,923],[611,1950],[1444,706],[67,2385],[240,1213],[787,1371],[684,1816],[1351,670],[909,585],[873,463],[3000,443],[546,1849],[900,2526],[431,595],[2583,557],[200,2626],[229,2436],[2710,1982],[326,331],[194,2081],[1422,2750],[1255,1755],[1451,2702],[1243,2983],[2714,2235],[383,565],[2011,2376],[1081,138],[981,116],[379,1985],[1831,663],[1314,1741],[872,234],[2200,1431],[1953,1023],[2474,1793],[1091,690],[2074,1935],[907,850],[974,2378],[2406,373],[2639,371],[567,983],[1208,1071],[2508,1754],[2457,2437],[9,680],[579,2164],[761,2088],[1852,2295],[2726,514],[1020,2995],[2079,2370],[1823,1983],[2358,2344],[2809,2254],[1267,1747],[1015,2465],[112,489],[2816,23],[2973,2118],[285,117],[805,1101],[376,2266],[2846,861],[1120,61],[1790,359],[2949,1227],[2717,1649],[954,2674],[1393,2761],[679,1512],[1252,6],[2661,210],[2297,901],[1958,543],[1901,1268],[586,997],[256,2065],[1688,1774],[1163,2328],[1706,319],[441,1371],[1943,906],[705,2111],[1035,2786],[2743,174],[2388,875],[2634,1319],[280,1913],[312,2933],[514,106],[2102,87],[1094,1843],[1470,1691],[913,73],[831,2117],[672,2049],[712,2624],[2263,2123],[2993,28],[2985,1770],[2045,1557],[2209,1862],[2943,1264],[2128,2501],[1463,319],[1490,314],[108,730],[2840,2599],[851,2467],[1465,1873],[2370,506],[2764,1312],[444,263],[1059,1433],[1581,1379],[803,1360],[1778,2764],[764,1938],[895,434],[1647,2699],[161,896],[1799,489],[1442,2012],[1454,2759],[2523,1925],[359,1280],[1547,1044],[1903,1659],[393,1120],[2436,2350],[1537,722],[2161,83],[1833,1665],[1862,2020],[926,806],[363,1904],[27,1995],[2616,2663],[2269,940],[946,2945],[2326,1939],[2489,1092],[2629,1676],[834,761],[644,2979],[195,2302],[2679,2452],[211,2711],[1118,1495],[2805,625],[1379,2966],[76,731],[2520,2820],[1378,1731],[765,773],[471,1733],[2121,81],[2271,1806],[2520,1982],[2020,487],[1441,2113],[1155,452],[1650,631],[1621,40],[1582,2928],[2193,2078],[1361,1685],[2443,2884],[1316,2873],[1298,588],[266,1372],[725,551],[2287,147],[1228,2573],[1060,2967],[2546,423],[2340,821],[137,655],[1517,1783],[1934,1917],[1934,501],[165,739],[1788,2338],[960,2459],[2510,2737],[1688,2438],[2959,2138],[2914,1427],[2970,2231],[2635,1877],[1736,297],[844,951],[1364,1832],[1930,384],[668,2898],[2242,2792],[2356,69],[2821,1279],[2292,1550],[716,2514],[1079,2595],[1044,1617],[2218,693],[1856,1149],[2613,2687],[1799,1268],[2953,2958],[757,2405],[2054,1326],[2915,1324],[562,2268],[420,1239],[1695,602],[2977,1619],[1810,2354],[573,1547],[2741,1317],[816,558],[1613,2479],[1916,2543],[1990,2458],[1545,2304],[1916,362],[2187,178],[1379,2041],[611,767],[1937,1232],[889,883],[2815,1037],[2873,1045],[1312,867],[1725,40],[2257,617],[2840,2055],[2557,1130],[2489,2963],[1685,2467],[1774,2450],[29,799],[2032,2726],[665,132],[1713,1912],[1632,2827],[1133,996],[738,338],[2470,1899],[2765,403],[445,402],[2402,923],[57,1881],[465,2931],[1350,1838],[2689,416],[2423,253],[2954,1756],[2426,2176],[1994,291],[449,1223],[673,2477],[2508,2548],[2074,2995],[2931,2749],[1832,869],[45,370],[615,1840],[647,1211],[591,799],[1877,280],[2224,269],[1532,541],[1810,737],[790,1197],[2749,1640],[2129,2302],[133,1736],[2050,1015],[297,2671],[2523,1998],[2942,2525],[2928,2863],[1575,2973],[778,1913],[774,1734],[1472,1330],[882,2695],[2609,213],[2246,1598],[2961,2230],[2328,2208],[1877,2144],[2632,2709],[2782,2450],[2394,1262],[767,2070],[1082,2927],[1844,2945],[933,826],[2144,2882],[1353,2751],[729,1236],[1494,671],[2513,852],[2960,2795],[2800,1092],[1157,2748],[2657,2178],[1047,2563],[2846,2730],[884,2120],[2244,2961],[1708,1833],[2635,1438],[72,2787],[2505,1711],[298,1424],[760,2657],[2837,1936],[959,1647],[1485,2060],[250,2274],[25,2396],[2025,1027],[66,2370],[2054,607],[2177,488],[319,415],[2660,249],[529,2429],[518,1149],[887,281],[187,1020],[1099,1557],[2593,1884],[834,1210],[770,2132],[599,615],[2963,1801],[1331,1151],[2653,1238],[2654,70],[740,2371],[157,654],[1632,2002],[1272,226],[2901,532],[803,2019],[788,583],[2381,447],[347,782],[729,2013],[546,419],[583,1782],[1165,1845],[1843,2034],[859,2633],[1997,2732],[2648,817],[2425,2577],[1193,2718],[451,1521],[2063,663],[873,1684],[910,1749],[1712,2959],[1653,2365],[565,57],[2990,578],[885,2944],[2725,1959],[882,173],[1277,2196],[1969,1435],[2116,1269],[481,536],[1953,806],[2985,174],[391,52],[2402,2664],[2092,1673],[2863,699],[1337,218],[1795,1068],[2689,580],[2184,1965],[2626,1605],[509,1582],[2438,1376],[1406,1667],[2524,2891],[1658,2433],[218,611],[903,1049],[1997,2839],[53,2921],[1844,2996],[668,1640],[1378,2223],[239,1995],[863,587],[109,2485],[920,2345],[1815,116],[1688,625],[362,603],[1174,2766],[1667,1885],[212,2150],[2287,2733],[807,1038],[1788,1244],[2315,2618],[2336,2269],[746,141],[1320,15],[1676,1106],[820,49],[520,2550],[2039,2712],[2673,1055],[1622,2409],[449,2907],[1440,528],[792,345],[2491,2857],[1309,1787],[2897,469],[2383,1663],[149,2920],[2264,755],[1413,1071],[2379,864],[1616,1240],[1709,640],[944,1550],[2043,108],[1634,573],[2386,295],[2396,581],[2700,2383],[464,2974],[633,2737],[1011,719],[1821,151],[2319,1347],[1712,2648],[1638,2090],[1643,2828],[2956,1594],[2442,2053],[441,1798],[1804,788],[1096,2098],[1034,1654],[1191,1286],[2249,1490],[575,393],[2748,1619],[181,2114],[2073,791],[2480,333],[1829,2226],[1940,629],[1178,1252],[824,1229],[1204,2760],[138,2348],[1241,2324],[2444,799],[1509,1900],[39,1777],[1241,2275],[2052,6],[98,913],[2571,478],[359,802],[425,2082],[525,2592],[2051,1577],[577,2951],[1288,2439],[2551,1018],[1541,1633],[2050,1501],[2805,1588],[103,2763],[2172,1449],[2140,1505],[42,556],[2772,619],[930,2592],[2797,495],[283,356],[1964,979],[494,2195],[2089,516],[2925,876],[855,1626],[2297,16],[2772,754],[1866,1243],[2042,2549],[1506,2764],[100,674],[171,2299],[318,1258],[2331,2705],[1135,1006],[13,2687],[1692,1581],[2722,2101],[2783,1822],[2487,1686],[2503,2403],[1849,2846],[2578,1878],[2232,195],[1962,2666],[2361,1239],[1460,1977],[163,1350],[456,954],[1359,1154],[393,2120],[364,1475],[2428,1538],[1464,951],[651,2147],[2809,1716],[470,1933],[276,450],[2545,109],[1800,1569],[459,2601],[1575,210],[2557,2786],[1385,333],[1412,2582],[2602,2982],[858,2181],[691,2490],[2903,715],[1748,1958],[518,2791],[824,1830],[2459,1590],[2547,1006],[1121,2894],[1655,1480],[468,2793],[627,2081],[2740,373],[2811,972],[592,232],[1804,784],[858,1562],[2979,541],[2827,2651],[2270,1738],[2767,2159],[2647,653],[336,1514],[2196,352],[1104,1226],[1378,2703],[385,129],[2625,889],[1205,2472],[525,1445],[2367,2109],[2933,329],[1623,1498],[2240,886],[2892,1988],[2947,429],[2696,1310],[694,1533],[2888,604],[1559,278],[1288,1782],[1297,2908],[2460,896],[1484,168],[1709,546],[85,1418],[2999,1172],[2816,1759],[2212,1623],[2016,2500],[279,2157],[1874,2103],[2164,47],[2520,1771],[1876,696],[1563,309],[2061,2639],[2332,2001],[1534,1771],[1000,2828],[1635,1385],[1723,2531],[1895,636],[1121,1661],[2320,1840],[1816,909],[2914,1294],[273,2271],[1573,201],[1224,673],[535,1078],[2086,2888],[1082,186],[548,1329],[1433,532],[887,1768],[1837,415],[2814,2094],[1214,733],[2167,1028],[631,2063],[1666,2098],[700,1452],[2490,961],[2508,2564],[2894,2085],[1797,878],[2579,1404],[2738,2941],[2112,2086],[471,133],[1909,958],[2380,1851],[2138,1369],[2154,1561],[2191,1195],[1410,2693],[1744,2077],[1819,187],[1493,2660],[144,2697],[1774,864],[2750,2872],[2070,1841],[2262,721],[524,223],[2150,2974],[1235,2637],[2810,2111],[686,2210],[1737,1564],[2631,2104],[597,2395],[663,2662],[1692,1541],[885,1068],[2405,2135],[2489,396],[1231,869],[2675,2667],[2084,1140],[1909,2329],[2193,547],[2587,1708],[2841,2173],[654,784],[270,1892],[2510,1001],[669,342],[1863,610],[2857,769],[823,310],[2182,2582],[2290,1637],[1472,1872],[1283,435],[104,823],[179,519],[2806,2226],[295,2229],[282,552],[1703,1356],[2912,2288],[1059,790],[2377,2601],[2649,1634],[2946,162],[2352,1285],[2048,724],[754,421],[2738,997],[1748,2814],[2609,467],[2310,142],[1405,2818],[2100,2809],[577,2906],[2614,334],[1900,137],[485,894],[325,2285],[2315,2391],[1904,505],[113,2481],[780,231],[1360,134],[287,1833],[1942,1175],[1943,1052],[2252,1002],[1676,278],[2018,2155],[2538,677],[285,1178],[110,848],[398,1795],[576,1283],[2872,2255],[563,2538],[1921,1975],[2609,2560],[888,122],[97,2481],[781,1475],[30,358],[1539,1024],[214,2090],[394,1438],[1208,541],[2709,1036],[350,431],[2372,2518],[333,1162],[423,1512],[527,1648],[2539,1641],[1374,1548],[480,245],[598,2629],[1962,2577],[1012,249],[1153,1743],[2861,1063],[1000,1029],[2099,2903],[1354,2765],[336,609],[267,2360],[2170,95],[2054,2917],[1055,143],[2603,1207],[1893,831],[2106,1508],[2749,2671],[1943,666],[2332,309],[1505,93],[1615,690],[2027,1705],[402,1530],[817,1101],[1289,1245],[1528,2214],[1919,679],[239,190],[642,860],[1836,352],[742,1415],[2298,1443],[2253,1734],[419,2841],[1611,1980],[1662,2841],[148,701],[2999,2671],[2935,2559],[450,1600],[1467,2907],[2860,467],[1873,1923],[477,1672],[862,789],[1215,2580],[2571,7],[2371,2644],[939,127],[1595,1917],[945,2387],[2057,641],[2965,2661],[374,2984],[1794,1469],[2990,2194],[2080,1593],[2405,1636],[688,183],[1827,2412],[2169,1337],[2607,1783],[965,1835],[1317,917],[2563,904],[340,488],[1924,175],[1814,479],[2652,1817],[85,2323],[1201,2870],[8,1587],[355,20],[1871,478],[23,2048],[2519,155],[2100,1401],[1369,1634],[2594,288],[2527,259],[1608,2681],[2651,1979],[2981,2789],[1067,2763],[890,1511],[1109,2174],[762,1559],[1546,1966],[2580,707],[833,1206],[637,2051],[483,2044],[2384,688],[1939,822],[1071,772],[1168,2639],[1950,2806],[375,1259],[1307,822],[1423,2185],[2715,1909],[2810,2355],[2942,1795],[1164,170],[1219,941],[537,623],[1114,1189],[517,2118],[2945,23],[240,2661],[909,1687],[2836,984],[1598,130],[942,2420],[557,1933],[2983,2324],[1752,2374],[54,2182],[2820,2293],[2844,1908],[790,635],[2375,460],[353,981],[2283,720],[1663,2485],[1373,1613],[1051,2145],[669,776],[817,1149],[534,2815],[1565,2102],[900,2031],[670,1496],[2504,1511],[2289,2901],[2162,1237],[1595,598],[2619,433],[1078,2026],[2229,220],[1780,2119],[658,2668],[1633,213],[2843,309],[2153,1986],[1391,2099],[2753,637],[2457,1970],[1054,450],[777,485],[2767,1627],[1293,2263],[701,2071],[1056,1834],[583,1437],[100,987],[1237,1300],[2776,944],[2434,176],[2640,1347],[100,2779],[2240,1621],[1858,93],[993,1658],[2768,1516],[912,2498],[1369,1482],[814,425],[2438,2419],[1469,2807],[1559,2625],[2123,2453],[698,656],[991,2482],[1022,476],[136,1249],[1769,298],[1953,2990],[165,967],[1842,1109],[2032,1303],[2736,2621],[1768,2807],[2222,570],[20,830],[2554,141],[1524,2340],[2747,763],[1024,2829],[761,1874],[105,426],[260,1066],[2369,900],[1293,279],[2541,2567],[1995,420],[2022,1082],[639,282],[2554,2592],[592,1327],[2000,214],[857,1612],[2182,37],[2471,2941],[1626,2793],[1961,283],[177,1095],[60,1570],[151,1080],[735,1170],[766,2736],[2143,2796],[1098,2545],[917,2424],[1290,295],[1775,2512],[1411,1622],[542,1735],[1855,2529],[707,1990],[2419,2666],[543,1809],[1270,2072],[32,1351],[2586,845],[2414,1696],[1761,2952],[1980,492],[199,1139],[445,83],[1478,1700],[910,2042],[42,524],[1739,154],[2717,1554],[1726,360],[567,2025],[594,714],[985,86],[2163,2415],[2466,135],[782,618],[2780,1223],[2733,2736],[2507,2],[500,2563],[1936,2389],[2781,2358],[258,2732],[2555,841],[2723,207],[2377,1664],[2146,860],[2262,2514],[617,1553],[2359,41],[568,2160],[1950,1278],[1306,107],[1941,607],[1923,2542],[1261,801],[1695,336],[1555,2787],[2095,113],[2382,2368],[2186,2210],[2389,423],[1121,2915],[1716,413],[840,1387],[2468,1786],[16,566],[2363,456],[2316,691],[1064,2789],[1081,2692],[1658,1133],[66,1360],[1423,1005],[1918,2545],[1904,2410],[736,1494],[1755,1543],[2422,648],[90,2998],[2220,2634],[2473,1964],[1948,1480],[2814,1650],[787,1462],[1342,97],[387,1863],[304,778],[557,426],[856,2600],[683,2547],[2730,190],[1238,2591],[2353,2982],[2167,1693],[2014,384],[2211,2582],[2204,953],[1174,217],[1741,2204],[838,2929],[2051,1731],[2116,1924],[65,1526],[1893,1197],[155,624],[741,2259],[279,148],[1015,987],[2950,650],[626,2993],[574,1579],[256,53],[2385,556],[618,7],[2692,1997],[2177,284],[135,386],[2966,827],[2445,1645],[797,2089],[2502,2459],[1373,2206],[318,181],[973,2530],[2493,2360],[437,128],[446,2257],[1160,974],[1570,2531],[2787,2912],[142,1507],[1155,354],[1195,552],[1100,2866],[2089,500],[1245,744],[57,1533],[2018,955],[514,577],[2875,14],[1439,2153],[729,1606],[1153,1057],[1932,290],[1239,2063],[328,2097],[1451,2986],[793,802],[216,1242],[482,5],[895,1683],[1103,50],[1367,1488],[134,227],[2414,1356],[1295,2043],[2115,2576],[880,2565],[2743,2933],[70,2059],[1282,578],[1204,2703],[852,865],[1713,683],[1747,1222],[1936,765],[489,314],[984,2466],[283,1257],[2756,1478],[384,425],[130,696],[567,629],[772,510],[1478,677],[478,1090],[1342,138],[2035,505],[1009,1894],[2635,2612],[1842,2720],[815,1185],[986,320],[493,2121],[2041,2290],[2072,2696],[2734,1678],[587,2831],[1668,964],[2198,2035],[1271,649],[1581,500],[548,1497],[710,2442],[1577,1548],[225,2858],[248,1209],[1348,2243],[1469,709],[1160,1519],[1184,444],[2415,1748],[2688,652],[1628,112],[346,1438],[381,1187],[424,1130],[853,2819],[1409,2554],[2053,1446],[1224,2793],[173,1362],[2774,2725],[1023,1331],[1048,1492],[1209,485],[2299,2137],[2014,1076],[508,554],[291,1850],[365,2221],[537,1526],[924,2555],[1724,816],[1298,1143],[613,1817],[421,1571],[2863,118],[2485,2650],[116,2960],[1578,691],[1825,1109],[408,2595],[1786,580],[162,1740],[1494,1454],[1488,1229],[1511,1325],[2944,1111],[1543,337],[2103,2362],[2493,586],[2088,1037],[2160,1110],[580,544],[2953,1075],[290,2303],[415,2162],[1086,400],[1999,2286],[245,2339],[1749,25],[1841,1288],[1976,1865],[1055,616],[2185,2722],[1609,2727],[1211,547],[352,2690],[2174,738],[1841,1501],[1769,2280],[2073,2358],[1932,1038],[2541,710],[2853,2767],[2069,360],[2500,2102],[2236,1392],[1372,1819],[2290,1657],[1141,671],[141,456],[2310,2294],[2156,594],[1031,1334],[1498,117],[2536,1509],[2428,1956],[2745,1590],[1899,1416],[2637,201],[2752,250],[2001,346],[1085,2440],[376,2584],[15,1267],[604,1745],[593,368],[978,1084],[2057,750],[1203,87],[2410,1794],[374,1553],[2127,642],[172,555],[93,2357],[1772,1555],[633,2957],[2145,143],[2597,2588],[2306,2014],[1964,2829],[2868,616],[1854,1344],[2586,1263],[1127,179],[655,99],[2677,1467],[2126,1843],[1897,1401],[185,1565],[2569,2189],[2366,1136],[1984,462],[303,1189],[792,977],[355,388],[2779,1984],[2839,2088],[2832,1643],[1981,1789],[1599,1720],[399,1304],[1184,1660],[1955,2785],[1103,2120],[2807,2568],[1556,804],[810,951],[48,1473],[2430,2252],[1019,1949],[235,2369],[2924,1123],[701,2037],[2168,2759],[1497,2118],[2707,914],[432,536],[2755,452],[2715,247],[241,2313],[2763,1687],[2895,2744],[356,2415],[104,2789],[992,638],[1758,466],[2616,2665],[134,251],[1374,1354],[2249,1078],[1549,2269],[1820,31],[1307,2487],[2604,2156],[2956,1269],[1103,985],[1135,2181],[688,2727],[1162,540],[1375,1396],[268,1707],[142,94],[1868,75],[2917,866],[2128,2734],[1185,1411],[1474,2383],[1812,2473],[2911,1587],[270,1429],[1892,2543],[1812,1656],[746,2905],[2669,936],[2515,1690],[1954,869],[2726,1673],[1693,2325],[2013,636],[2064,2240],[1004,2699],[2675,1256],[1973,1930],[2806,595],[2447,2324],[194,1595],[1215,2684],[294,977],[2378,2139],[765,1562],[1510,2926],[881,2455],[1654,2737],[2385,162],[2071,2056],[2965,2241],[2883,498],[804,1134],[1200,2866],[1737,1694],[2429,1784],[2157,759],[14,987],[1193,2428],[45,1834],[1965,2305],[1234,1856],[1463,517],[972,2062],[606,1244],[454,247],[1330,1063],[739,2251],[848,2389],[1778,1414],[1593,2091],[2446,576],[1901,474],[166,2036],[1629,39],[566,2569],[2314,635],[2838,1143],[2163,475],[2327,307],[2227,281],[722,842],[1088,1200],[2143,2912],[2786,1917],[308,1529],[1051,1922],[2896,931],[1046,1756],[982,1891],[2534,2950],[1523,559],[2506,412],[360,1644],[374,132],[2010,1266],[2176,931],[1143,348],[545,235],[1134,2189],[71,89],[1397,4],[155,1614],[2929,653],[167,833],[280,687],[800,1921],[335,1231],[1832,656],[1739,1348],[2818,1454],[410,446],[2149,1060],[2997,1487],[1868,2472],[2378,395],[2235,551],[780,1571],[1798,494],[2957,664],[2859,504],[175,2607],[2236,2869],[337,1513],[248,2757],[1033,2741],[2044,935],[2741,1957],[2788,2642],[1679,2307],[1420,646],[1573,398],[1766,2587],[1861,288],[1641,1356],[1146,819],[1501,1145],[650,1970],[1018,1471],[1781,144],[2039,99],[2208,2728],[1002,1573],[624,1974],[2212,4],[428,1770],[876,1001],[228,925],[2889,1949],[428,1433],[2056,1967],[179,2017],[2134,220],[121,2478],[2052,1811],[1930,2618],[2218,1630],[2364,2823],[476,1869],[321,432],[29,1256],[1764,351],[1263,866],[664,2013],[2800,1286],[344,2698],[2552,723],[572,533],[1523,775],[40,1052],[1651,1502],[1971,483],[2991,2376],[2822,2575],[328,658],[1391,149],[2046,1322],[1326,2778],[2687,566],[1621,2091],[1147,2100],[2218,1066],[1259,831],[1479,695],[901,657],[2234,51],[471,996],[2355,1669],[1151,922],[2294,1683],[2423,1295],[1268,1618],[52,1751],[1386,2019],[626,2259],[703,326],[2404,2183],[2443,1164],[2040,2847],[1898,1038],[2949,1744],[2261,695],[257,2930],[484,2027],[2519,382],[2889,2347],[156,84],[2217,1351],[1760,973],[605,2677],[2188,522],[2255,943],[2774,1707],[296,2669],[265,2721],[1182,1599],[1412,498],[2393,1145],[302,1123],[2550,2992],[2700,2040],[648,64],[618,2803],[1148,1871],[2851,2892],[64,1667],[293,1785],[1248,458],[634,695],[2284,2466],[1946,533],[1715,2245],[2665,2036],[2695,1847],[1113,1513],[1886,910],[34,137],[2590,2031],[1617,2980],[1881,1148],[1606,2411],[1906,752],[1602,678],[1074,2830],[330,836],[991,1533],[1333,1801],[1339,1230],[392,810],[2059,2616],[713,2864],[1113,811],[1355,480],[1163,2136],[273,1719],[1456,670],[47,843],[2226,363],[1281,307],[1884,2124],[329,2365],[1325,412],[1926,2775],[153,2861],[565,1813],[2493,2206],[126,31],[1279,33],[549,814],[2335,1578],[1989,1089],[220,2458],[2731,2693],[1407,2113],[149,2713],[635,361],[736,1963],[77,481],[662,294],[2387,2591],[1803,1003],[638,993],[1718,1003],[1990,1487],[2952,302],[2076,2156],[2258,1084],[2483,929],[350,2418],[2746,1056],[1884,1679],[2834,2067],[594,321],[683,2614],[2300,718],[959,2694],[2754,532],[1883,1179],[1977,1226],[2230,2254],[90,2509],[2221,2657],[396,560],[2175,2320],[1203,2756],[2490,1845],[482,2856],[522,71],[1601,2574],[2516,1224],[1381,1166],[476,277],[843,1797],[1255,1473],[2179,2642],[2643,2408],[1456,329],[289,2541],[1347,2895],[632,582],[519,88],[1161,2530],[794,2454],[2272,2101],[1217,2482],[1514,1697],[2603,848],[1754,2758],[9,1292],[2522,511],[50,2225],[1299,342],[1275,786],[2884,237],[1582,24],[2144,1259],[1613,2957],[530,821],[1196,1394],[659,531],[2300,2610],[481,2935],[2095,263],[2319,2777],[1709,2135],[2445,354],[1389,311],[2484,2758],[2055,834],[308,1758],[1826,2050],[2682,941],[2648,1217],[1021,633],[79,1355],[1777,1102],[2069,773],[2830,898],[152,1703],[1898,2849],[2587,1330],[1776,2926],[1062,2631],[271,2185],[1891,2343],[2483,529],[2919,231],[1343,2173],[2056,2060],[2316,2537],[451,2291],[1120,2830],[1828,2998],[2172,2551],[1030,389],[2195,2941],[1129,2678],[855,604],[2242,2031],[1060,2141],[858,2712],[2130,60],[520,264],[2801,720],[2234,303],[191,1636],[2757,150],[2860,1287],[2174,1839],[1464,2790],[722,1820],[83,2850],[2675,1408],[630,2417],[1759,1857],[2684,2262],[277,1701],[2981,2674],[377,538],[2836,672],[603,2476],[1928,1628],[915,95],[1557,1436],[1477,2514],[2006,300],[2340,543],[1181,55],[2938,1107],[1221,947],[1310,2781],[1602,2332],[619,1865],[1012,176],[1333,1704],[1702,1699],[1272,1155],[872,1252],[2643,163],[1144,2744],[2125,1355],[1512,1263],[364,43],[2615,2072],[2571,814],[1257,1540],[2819,2285],[1031,48],[2555,1610],[1792,2373],[348,1177],[1128,1789],[1781,640],[626,1699],[43,1528],[1187,1779],[924,988],[932,1847],[265,948],[2296,2688],[156,405],[957,492],[300,979],[1218,1220],[361,2094],[807,2359],[1705,2631],[2813,2283],[438,2412],[2155,457],[454,2155],[411,1824],[801,1173],[515,111],[31,1284],[389,1374],[1935,1480],[850,1358],[2403,2446],[1951,2710],[2334,1014],[2638,2136],[1996,2322],[1914,624],[1096,2988],[697,2533],[1701,2821],[2180,2213],[2408,760],[206,407],[959,2937],[497,1851],[2234,2796],[1638,621],[2745,2591],[2700,780],[2915,2528],[1163,2151],[1704,1571],[2168,877],[1644,827],[2006,2818],[1899,2718],[86,2665],[1122,2085],[2039,2205],[2437,2769],[461,195],[1237,1181],[455,1256],[556,1929],[1903,399],[1225,2034],[2477,1775],[2731,1087],[341,2600],[2411,2064],[2008,2784],[452,1839],[1746,2216],[1996,2242],[391,1971],[734,1011],[1603,568],[2446,978],[1675,1192],[2238,299],[2093,1251],[2344,2825],[2302,915],[2122,630],[416,51],[1430,1376],[474,2702],[605,1177],[1885,836],[2546,1407],[968,783],[1977,2279],[2094,2250],[2314,768],[1646,1684],[1535,1167],[2165,893],[2560,32],[1850,1232],[2885,806],[843,1],[968,2887],[1481,1022],[1570,2775],[1173,192],[620,2739],[258,1725],[2999,502],[1566,553],[2551,1700],[1655,555],[2971,1189],[2373,1470],[1377,853],[2122,1075],[493,189],[2662,2173],[275,125],[649,2645],[1576,182],[1446,1857],[2525,151],[2417,2449],[1925,2857],[1370,717],[2373,1394],[2496,14],[1462,528],[800,2298],[1349,1783],[2975,2644],[320,1052],[2022,1729],[2356,582],[1495,60],[600,2334],[2881,929],[2921,802],[2955,1073],[401,1440],[2361,1136],[1317,2711],[1671,2468],[1666,1243],[1106,2640],[833,747],[307,1701],[206,2893],[275,1024],[1190,1112],[989,1612],[2632,2723],[1589,269],[2355,315],[982,1807],[1493,2618],[2397,539],[602,1636],[1729,1320],[2216,2574],[850,2007],[2058,2443],[2225,713],[2330,1620],[2092,2529],[1459,2448],[998,1600],[74,61],[435,1443],[2049,2475],[449,403],[2938,879],[2524,553],[1229,1421],[1502,1363],[1792,2826],[1891,2706],[2707,526],[278,101],[1867,1979],[164,2228],[2006,2179],[1888,232],[224,1357],[271,171],[1905,1940],[2388,2023],[428,421],[1174,1671],[1863,1116],[165,168],[1373,2305],[2363,2773],[868,462],[2567,246],[2919,293],[2596,1389],[2842,808],[1262,1362],[2471,2425],[213,1475],[1782,2412],[2279,1041],[2565,1276],[1711,1008],[1445,680],[2930,353],[1539,2655],[1632,1273],[2108,1822],[789,1201],[2372,1584],[965,2522],[634,2024],[418,1668],[1495,306],[2497,1425],[2047,2739],[19,487],[1025,1588],[1552,1313],[1184,1000],[1093,1258],[2783,321],[1563,2376],[1601,948],[1693,2921],[1651,713],[2404,304],[1254,1087],[1760,1053],[1435,243],[2911,2650],[480,308],[1168,824],[1803,717],[1029,1691],[1529,56],[1035,1633],[1538,664],[2184,2637],[2699,2691],[2127,533],[2431,2677],[2134,744],[757,1813],[317,432],[105,1246],[2918,249],[1648,424],[372,1173],[2531,2908],[2030,201],[284,972]]) == [1, 2, 3, 4, 1]
