class Solution:
    def _check_even_valid(self, nums, pos):
        if pos > 0 and nums[pos - 1] < nums[pos]:
            return False
        if pos < len(nums) - 1 and nums[pos + 1] < nums[pos]:
            return False
        return True

    def _check_odd_valid(self, nums, pos):
        if pos > 0 and nums[pos - 1] > nums[pos]:
            return False
        if pos < len(nums) - 1 and nums[pos + 1] > nums[pos]:
            return False
        return True

    def wiggleSort(self, nums):
        nums_sorted = sorted(nums)

        left, right = 0, len(nums_sorted) - 1

        while left <= right:
            if left == right:
                nums[left * 2] = nums_sorted[left]
            else:
                nums[left * 2] = nums_sorted[left]
                nums[left * 2 + 1] = nums_sorted[right]

            left += 1
            right -= 1


    def wiggleSortBruteForce(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        for pos in range(len(nums)):
            if pos % 2 == 0:
                if not self._check_even_valid(nums, pos):
                    for new_pos in range(pos + 1, len(nums)):
                        nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
                        if self._check_even_valid(nums, pos):
                            continue
                        else:
                            nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
            else:
                if not self._check_odd_valid(nums, pos):
                    for new_pos in range(pos + 1, len(nums)):
                        nums[pos], nums[new_pos] = nums[new_pos], nums[pos]
                        if self._check_odd_valid(nums, pos):
                            continue
                        else:
                            nums[pos], nums[new_pos] = nums[new_pos], nums[pos]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.wiggleSort([5420,4255,5103,3492,2509,931,3637,1980,4860,5779,5690,3957,4023,1731,84,1172,1716,915,1771,6875,112,2954,4989,4546,2528,1669,2848,5219,2861,9,5264,1142,5879,481,5888,2272,3292,3338,1070,5642,2642,650,3134,1203,5028,5469,287,4009,5617,2245,1710,1320,4169,547,2914,6669,3616,5740,1100,5036,2837,3634,2710,6297,4580,2355,4594,5422,6913,1776,1750,2490,4451,3168,3222,2902,2075,3881,5780,3396,5079,3250,6747,2470,5618,2815,3902,2933,6482,2942,6835,6363,1152,3311,6916,6454,19,2812,5150,175,6922,6116,3685,2236,1575,5558,6380,1418,3835,4766,6772,180,4751,1761,3323,4787,5680,669,4653,2878,3432,842,2881,5599,3454,3602,1273,3262,6410,1460,4144,6749,1459,6160,4959,4139,6647,3546,971,3993,4195,1468,287,449,3662,1857,1934,5605,3303,5464,3099,6815,5491,4370,816,3030,2961,6706,6955,4015,6005,1456,1660,2592,5064,2938,6639,1353,2344,3820,2975,518,1031,3208,6642,5763,1182,2452,1120,4861,5652,2182,4527,2025,29,4330,4751,6992,1650,6135,4017,4254,5495,6742,5907,4015,2820,5054,3265,2124,697,2007,944,692,1231,371,5209,6014,5948,5328,6001,1459,6719,1662,2502,2948,1511,1362,5240,4410,4238,2093,626,480,1018,1093,5480,2186,6658,4313,6435,3002,2265,5708,4897,4419,5781,6430,4174,4170,5547,2518,4776,1137,5172,5456,4779,1026,4462,397,2412,2911,96,492,6660,3559,2270,4945,797,2242,5489,6381,5404,414,1802,4930,3205,6748,5382,5450,5604,813,6927,6698,4514,4493,633,6590,2532,1305,5693,6278,4472,3148,5845,995,1366,6279,577,112,872,243,417,2531,4132,1414,20,4881,702,766,1251,6496,1122,3758,1062,3054,6011,1171,5020,4484,5479,5395,573,4465,6741,2126,2922,2511,6057,5965,3435,2258,3475,2219,2323,1406,4773,3148,1909,4761,3432,6999,3733,248,2341,3438,6687,5632,4467,3396,185,3114,5901,1014,5328,31,1730,5574,6040,174,2760,1536,6359,4370,3842,6185,242,701,3682,335,634,3779,4269,4491,5361,1380,6396,3833,4930,2846,5105,385,1092,1613,4613,1734,6583,3174,100,2599,5539,3776,3508,533,3041,5290,1954,4896,3072,1470,4121,4542,3151,3895,2623,1688,1483,5844,2817,5358,6595,6186,6507,3992,4235,3795,5478,2648,791,124,4131,4942,2414,5003,530,2490,768,3296,4891,1168,4886,695,2461,1220,4429,4067,6618,4483,6611,3367,4164,5910,829,4394,4975,5004,2003,3108,1337,5493,659,1721,1986,6722,1139,3421,6780,2197,4207,2347,544,5546,4533,6710,1993,2073,5439,6669,3596,3448,1375,3697,956,387,2050,553,1824,4704,6733,2476,5566,4945,2550,2240,5894,3882,4295,6550,3265,5820,5376,4641,1462,4387,6984,2638,3005,4566,6822,5552,3231,2213,4214,4921,3936,2082,469,6795,3844,4453,4413,4913,5517,2910,1313,5716,988,3713,267,3888,6201,1919,5153,4967,4993,389,4467,5601,6921,5378,366,568,2955,147,1207,936,6178,3533,1407,6335,5559,1555,768,4289,5883,4799,4094,2086,1670,1772,392,3169,6062,3706,5733,1293,6093,5322,4072,5466,6814,5760,4763,1144,1177,6803,328,5655,971,1462,2529,3162,3697,3542,346,637,2302,6264,4982,61,2976,4936,449,2203,6398,6364,6699,2228,1763,369,2476,2248,4930,2342,562,238,6419,4505,3090,4383,6834,1281,5520,2623,6054,4788,2492,2944,2768,1367,2330,5644,6745,3407,2453,3771,4181,3954,526,775,4295,5940,6545,5934,1552,4375,1445,650,5066,2285,964,1049,2658,3417,2861,1349,1236,6091,5778,5864,1185,1425,2185,2334,730,3474,3476,3869,131,2242,4497,5402,3001,1237,4003,5171,4696,4335,6340,3002,132,2727,5002,5693,4849,5292,5608,3540,5900,3075,5273,797,1614,3854,2887,4687,6221,4316,355,2345,374,4408,2895,879,5623,2467,242,3561,6351,3162,6909,857,5188,6691,4433,4592,6421,3396,2876,5849,2459,6739,110,3248,547,362,6137,1927,2779,673,901,6686,3596,6472,1059,1349,5878,5207,2487,696,6435,4472,1303,147,5021,5119,1713,5633,588,2296,1731,4028,4820,18,3651,4766,2786,629,1994,3609,3917,6023,4864,5737,5362,1543,1274,5108,4035,6826,4268,4654,5749,1288,1128,2408,821,5389,3499,4701,5002,797,279,2049,6192,3150,813,4241,2184,2925,5007,6609,424,95,648,5289,446,6495,5837,3306,3795,3352,1127,1985,2429,1665,3368,236,4856,6517,1789,5115,3182,5675,4794,5359,3666,976,6733,1027,4662,3683,5899,2018,5444,2402,2674,4855,5699,6588,2715,6678,833,2439,4900,1860,4375,970,4948,6921,4055,6236,154,6767,1590,5708,4943,5126,5172,4855,3777,1524,6194,158,549,4408,6340,458,4732,310,2138,2823,6839,5805,5139,1556,470,4933,468,3904,3023,6272,3831,2299,1318,5780,4394,1066,1816,1228,5945,6286,5473,84,5345,1842,5950,2414,2843,1345,6066,446,2963,1052,3006,5852,1598,2262,3492,1532,3569,5900,1585,5369,4178,6661,4463,1934,5505,1493,5693,3749,683,1592,1266,730,828,5433,4360,2193,5643,2676,148,6376,6830,1794,6817,3122,2089,6376,3719,5262,4855,6182,3888,474,2265,2184,2961,2696,3938,2789,1964,3625,252,4737,6738,4997,1322,2872,4897,3439,3107,3825,582,4246,4762,6907,5055,5801,5048,5319,370,387,5413,2178,5468,5131,517,6341,2049,646,1148,4078,2391,6191,4724,1494,3273,842,2293,4532,6439,6567,5092,922,1020,6586,6071,5969,5264,1017,1178,2734,6830,5038,6365,5778,6670,3614,2705,6361,5391,2934,5420,2029,5191,5557,4153,3638,2810,2786,5047,6974,4692,3153,1212,6270,1515,2529,1830,2179,1433,2876,4552,4328,259,4350,564,238,2324,6386,353,4058,769,894,2557,3417,2633,1715,1977,2116,2869,925,3199,3574,1466,2293,6729,1583,2692,3868,6025,6445,648,1039,4940,964,17,6984,1569,3968,4212,3629,2671,938,4551,254,6203,1180,2449,875,2567,1384,2449,5949,4358,5501,379,5995,3290,5930,2991,2949,4494,2482,2778,3105,4540,4990,2166,5590,3323,5750,2391,6248,1462,1528,4789,6124,5768,4200,4978,4930,2470,1640,5277,3595,604,2593,468,354,4877,5418,4437,5736,6460,5046,2826,4700,3849,2586,3436,6436,5551,1570,3088,5181,5472,843,2997,3108,4088,2806,5297,3532,443,5410,2583,4852,3437,879,4085,4739,3146,2655,405,4226,3843,2530,1885,2401,5572,6168,3,4633,6624,942,4059,856,6807,5053,6130,64,346,1107,2181,1793,6675,6302,4881,1950,1311,6012,5833,4265,3401,6934,2788,1587,2889,1467,1538,902,4399,2347,3189,6205,6082,3661,2775,941,1474,2668,1062,4175,6511,1522,6966,1459,1014,1300,283,3142,1188,754,524,6633,2284,6709,2236,2413,2412,864,3782,2698,4075,4694,915,5216,3864,5501,3958,6031,333,1562,3240,6126,5392,6490,4855,5453,2992,4826,6016,1965,5175,3674,678,5177,548,1652,6026,295,1559,2979,3851,4899,2389,1138,2620,2193,4276,3356,4543,5600,2074,4139,1958,1188,3587,2647,2962,2230,3659,3664,6105,4442,6744,659,3661,4465,6218,2987,1944,5280,5396,5291,3324,2763,5381,2076,2196,2868,5094,38,86,4302,2056,2642,6597,4338,6105,3121,4376,1309,6556,2099,553,979,1334,3423,3759,6340,448,943,3847,5328,6479,1809,4543,325,40,1778,6057,740,2340,5791,2963,1870,2893,2419,1462,1325,1095,1675,1296,699,5111,4457,3451,1718,6852,2775,4455,641,5623,4143,4811,6636,5880,393,4361,2991,4455,3599,4532,44,1137,2238,3572,4310,3983,504,4316,1074,6221,938,5799,4266,6552,5415,5508,6568,2721,5748,4982,3161,6473,2472,2246,2783,582,5857,5728,4400,3619,5240,669,5055,2641,5759,2243,3333,3627,277,2474,4646,1715,545,5221,4227,2992,276,6900,5328,627,3895,2511,5867,2937,5080,1279,4871,6958,4836,2934,328,6809,2503,3395,1232,6331,4859,6213,2657,248,177,4445,5636,6411,3067,6172,5877,4298,3543,571,1894,4356,1319,726,4551,3770,6598,2569,449,1392,1675,1217,6421,4870,4282,3068,2715,3327,4648,680,5034,5035,4020,3143,2564,5231,6643,4194,3411,3530,2119,6159,3896,4440,2411,3733,2271,3161,218,2222,1153,3013,4614,6107,2648,2524,4165,4734,4754,5753,4709,249,3358,6753,6318,1767,4531,1973,1497,4939,949,5755,5555,2993,3981,3689,2454,5136,6282,5574,756,2509,156,3199,2357,1101,2316,1086,3277,2720,5522,5697,1387,6938,1251,5146,1814,4985,5641,3607,6828,4802,4664,6827,3952,6064,4099,1976,6574,1009,2114,6980,2772,4161,733,1119,5402,6044,138,2610,5935,558,4906,3023,2965,2947,2726,5725,1083,1902,4343,5253,791,2244,6118,3048,4948,5970,3531,1851,3718,178,273,2493,152,1623,1087,5614,6734,207,6025,2066,3609,4633,2892,1944,904,3867,4242,5572,2284,5232,6696,6097,5192,4437,568,5752,4282,5275,3747,4689,3813,1181,5732,260,332,6043,3025,6621,209,2844,1838,5454,2334,2034,6311,150,3845,116,4744,284,5275,1564,4524,5513,4467,4561,5316,1693,5041,6616,4052,1909,1843,4687,2125,890,6037,4636,364,4571,2242,5476,2142,2398,1623,3403,3451,1796,5384,4392,862,6788,4585,521,4669,6304,276,6791,483,1808,3263,3204,3846,1174,1061,4941,1157,4558,399,2426,4916,6293,2889,6421,3252,2828,1941,6312,5797,6651,3084,5016,2472,522,6909,5521,1796,6014,1362,2332,1886,4177,3067,3358,4070,6020,6888,6694,6490,5648,3239,6814,1718,5347,6590,3017,324,832,4044,504,1885,669,1513,2338,1383,2805,2180,4738,3652,4841,3413,4510,5108,278,5265,3185,656,150,2310,1692,3395,633,298,6978,3655,6229,473,356,4918,6294,587,6301,1430,5771,420,5827,3786,4010,6675,3743,48,5466,4919,953,3598,864,5029,4368,4605,4007,6359,4321,4860,782,2562,6650,44,4212,2968,1188,4755,978,5633,6670,6405,1357,6585,281,2366,2907,883,426,4207,4610,5600,3293,1659,5471,4887,3878,5082,4808,6026,2477,5092,5243,4342,397,695,3559,336,4099,3775,1781,5813,3697,4923,2704,369,2746,1212,2085,2082,6380,4157,1928,4431,5967,6533,3802,5619,5254,3049,2438,4435,2924,2648,3273,6775,1961,3315,3521,731,461,3052,3868,6324,462,1596,1931,176,2256,5377,4465,4114,4687,6365,4720,1122,776,6679,6563,1854,5033,2850,2143,3926,5647,6917,2290,4434,5048,2090,5566,5010,2648,4574,342,4885,1988,3159,2381,3362,4166,6861,6473,3691,4243,6999,2637,665,2489,916,3678,3848,1297,2394,4135,4210,3315,3864,2268,2289,4100,2508,3745,5557,1541,6447,1999,5469,5469,3981,3542,6077,2882,4226,5731,3478,3367,2715,1935,4691,2678,5324,3123,4741,3927,139,4490,5789,5333,2719,4186,6265,2450,62,6653,4797,139,841,5248,2072,1407,2296,5322,5451,4921,2920,477,4558,6099,3604,5045,4973,1261,911,5059,2809,6966,3559,2895,4243,2118,6461,3964,2567,2616,5180,2923,5687,3625,5834,5131,1539,181,3728,2674,3670,5594,4399,1698,5172,430,5433,4510,3122,5748,5093,5440,3336,1064,6006,4460,3360,4253,2143,1953,6189,4666,3976,99,3463,5013,4937,3386,4117,749,3261,6312,3378,4706,3332,3549,4823,3549,5633,1241,5820,3179,3008,4707,2443,6489,4423,3583,5867,2362,481,5869,1524,919,1263,728,2353,3740,377,5939,5161,5800,870,4851,4788,1235,1539,6490,1768,3972,3338,6885,617,1044,2873,922,1646,6993,4131,4767,6576,6520,3278,4402,538,1065,508,4483,3271,1219,5147,2632,5386,5552,8,2186,1085,5471,5151,6429,4698,3983,4615,2839,5318,1393,5876,1202,5772,3962,5113,441,5105,1823,804,269,3128,3976,2653,1949,3156,2289,2409,1533,5554,4369,1345,3942,5266,2608,3759,6758,2763,3385,6116,5013,104,133,5314,3359,923,3040,1885,4519,4656,3295,3810,3447,3477,3356,6200,3162,5963,4090,2777,1103,3026,1972,348,6150,4954,4151,1585,4848,6883,360,5706,3166,6306,6237,1209,3780,3500,2982,2615,3651,6888,6261,6200,6012,5459,6697,4444,3849,5760,5290,2719,5599,6947,4943,670,5945,2320,4689,380,2796,4720,5317,6029,401,4491,3437,220,3935,3863,3862,5319,2137,5666,6787,501,577,3262,800,5515,408,1318,4266,5578,6385,1710,4236,3824,4309,2622,5268,2250,257,347,4634,5879,4517,5694,16,1850,6765,2071,2313,2506,5853,4032,4796,2150,6212,2694,2673,3110,2790,6009,3986,863,2782,454,3225,4520,4714,5431,3134,1405,3559,5464,2303,1243,1338,6785,6522,2944,1911,3610,315,6657,3942,4942,1078,3764,2641,535,1795,3716,657,6463,1489,5905,4496,4769,3902,5817,2825,3870,6838,1493,4830,1636,4437,6424,710,3880,4259,352,3386,4802,2695,3701,3843,708,2540,3351,3765,5426,1756,1955,315,2026,3024,6961,1697,4313,46,4326,6995,4594,4211,5262,4264,370,5767,4002,6357,5108,2018,1543,6753,6564,3090,3011,5875,2306,4755,1146,5989,971,4609,5763,2478,5491,669,583,1498,6776,5061,5129,5455,3158,2536,6331,2472,4055,6420,2397,1106,1665,4323,250,3753,6743,6115,2602,6658,6487,1427,2285,5913,5082,101,1775,6527,2476,5559,1375,2656,2363,2101,3865,6918,234,4453,2460,2740,1735,761,2621,2445,331,465,5256,5657,6723,5641,5968,6824,2473,2950,4316,1547,5192,4423,1391,6085,6415,3235,3133,5111,1846,793,6522,6532,2816,857,2808,3009,4903,4121,213,4528,2733,5673,4284,1160,4913,5441,936,6466,4149,5927,6413,1586,451,1735,6397,381,5222,2642,1765,4448,2267,1084,5821,5758,3050,6637,3404,5632,4530,2614,204,3267,4899,1233,2768,5462,5513,211,1405,503,6945,2520,1972,4213,5718,4857,2517,4952,3242,3677,4921,3671,6009,6594,6373,5932,6259,3062,4536,5797,107,3526,1494,2380,3721,404,6372,1201,2313,282,6360,680,5728,4095,1528,3134,5784,6838,1853,3221,926,2655,5765,3393,4472,5160,1555,135,803,4228,3737,5142,2798,3746,2683,4764,6945,4422,4812,3379,2327,1679,5742,6839,6190,5083,659,5239,5707,4725,6698,6825,180,5249,946,6570,4481,3921,12,1911,4683,488,3305,1863,2334,2640,1895,1095,5941,577,5492,905,5699,4876,6186,2534,977,6394,2112,4280,4092,5440,2381,10,4637,5261,240,2843,4858,5115,5300,6290,3339,4046,2133,5337,4509,1089,1116,3099,5465,329,5040,1768,316,5524,2993,1459,2170,642,6249,5661,2981,6893,3092,1024,5928,3597,4399,931,4195,3197,2277,2230,3421,2456,1708,4873,1516,5719,3495,3771,403,4903,3673,6444,878,3784,2048,1084,6088,3059,2359,1978,1197,162,4003,2183,5590,6664,6745,122,4318,956,6743,5056,1905,4609,2909,2645,6508,2315,6937,6019,1143,3151,6674,6397,2555,5490,2546,4457,244,968,2617,2138,4923,6949,4375,447,889,3887,417,4869,4679,5627,1147,6479,3347,3485,4528,100,2876,3827,5743,5464,2425,1440,5827,4691,5271,1593,6573,6802,4158,6638,2963,6115,746,4631,1036,643,3005,4865,5336,627,1698,1774,810,5038,3407,2036,1854,2295,4576,5647,1009,5426,6133,1907,5202,1799,3772,5052,948,2815,495,2618,2661,715,4164,3342,2251,1409,78,5359,5957,5743,1454,6677,3932,2656,4397,6780,1969,6808,1837,1357,3823,3307,893,6546,4099,4866,6773,2535,5439,4175,835,6775,6715,1130,44,6669,5400,5022,4944,3539,5096,3469,1294,5557,4422,472,1937,2313,4641,1050,2434,3276,2088,5222,4398,1086,77,4009,5057,5704,3348,5755,312,198,2556,983,2285,4972,2290,2871,2118,2512,1017,3517,49,5760,3597,1768,1884,4875,6404,2497,1937,1220,6144,55,314,142,4576,6372,6786,1588,2195,967,3321,736,1440,6415,9,5602,1724,1244,3523,5591,3863,4443,6090,3885,1646,4813,3232,5058,3942,1638,1203,697,717,5112,1719,3033,182,5205,6576,1788,4187,2979,6454,1346,293,4536,6307,5368,3619,1876,4106,397,3138,5687,6243,1681,4676,4928,1661,4531,5118,1336,5089,5817,2881,5478,4491,2796,3888,4915,1985,5160,4072,5060,1245,5828,5908,739,6559,4733,4191,1777,419,5398,6824,5948,4209,2020,5330,55,6205,4254,1076,3723,3720,5032,5528,828,1871,13,196,3972,6769,4697,6339,4181,1875,3095,1102,3950,21,1377,2477,6850,2634,6035,2873,6941,4862,1408,5374,5958,5893,6864,1053,2349,6847,3087,865,2727,4479,6698,645,2989,2272,2523,546,2923,4588,1320,1834,604,4245,5335,2783,2517,2325,671,3273,3014,6639,3980,418,450,2954,225,756,627,3575,4332,2197,4411,2741,1693,4669,773,303,2671,2021,30,6187,910,2227,4643,5394,2477,5352,3220,3192,522,5061,962,1781,5210,2016,6160,6524,4243,6591,6490,5915,3746,3086,100,3359,87,3677,2078,629,686,5461,3743,2076,1137,2507,1186,3878,3859,2243,1519,3040,2880,3301,4896,2747,3664,6655,3839,2319,363,153,22,1323,5191,2552,4592,3429,6456,2408,3286,4354,170,2973,3460,3495,4040,5296,5979,806,4592,4921,3265,5322,5411,5306,4066,4001,4514,3803,4664,6023,1567,3972,941,2681,4126,5972,6443,2659,177,572,2024,2948,5433,2300,4038,1549,4002,3802,1603,3195,3663,1435,306,4109,2686,5600,1725,6785,2763,2205,5628,1477,6583,895,581,6690,1960,3235,6984,3740,6396,3070,4751,2721,4996,478,2467,2818,5528,5399,1567,5126,481,5111,4236,1427,472,1727,2453,3456,2547,3114,3845,5227,1367,5842,1272,2407,634,3116,1278,4772,6379,421,4400,5558,370,6090,6454,2017,1444,2044,5324,4532,5905,2038,1372,103,5977,4399,1747,6908,2045,1099,2195,6517,5169,195,6717,5508,429,1171,5351,2940,2227,2026,604,3415,2666,421,1712,1223,2768,2915,6332,3050,5930,2147,612,6166,6197,483,1003,3051,4446,5650,5167,4832,5679,2822,4598,3716,600,4593,4608,273,2764,101,6167,6697,5752,1997,5934,6590,6446,1829,4123,2608,732,1810,4836,5828,6121,4149,2926,6505,3493,3154,5826,2154,3356,1483,6196,3336,407,1634,266,6508,1858,2410,2160,3724,5999,4044,5282,3513,2186,6378,3177,2925,716,47,3152,651,4966,3936,3063,2298,4733,5303,1533,510,2072,908,4312,954,527,5240,5608,3113,1706,6667,5332,3408,3576,2508,3062,4839,3888,3835,4550,6618,925,2957,5958,5817,3619,6819,5467,3488,3428,6054,5212,1634,3515,3430,1972,1980,6993,3186,3130,2193,5498,1095,1978,6232,3622,4587,3336,6129,5109,6407,5340,5952,2528,6166,4773,6967,1491,1036,6651,4885,6900,3868,3866,1331,303,677,924,4001,4883,1955,1022,6701,2445,3428,6371,5040,535,3639,2768,4999,4583,99,6305,3566,1427,3809,2173,6370,2777,1397,2192,4759,6189,3627,91,4809,837,4139,5352,6075,1275,5806,4638,3407,4538,340,1195,3980,457,1603,5069,2122,4963,4959,4627,3805,6016,3783,4635,99,3853,251,907,6904,1839,2930,5763,1675,1885,3627,6083,5188,3966,5690,4778,5891,1906,3809,237,5923,5273,969,6649,2794,2511,5073,3002,2047,1188,6556,3093,3944,3709,1625,4222,3434,243,1775,4669,2005,3949,4820,6028,3736,952,4381,6931,4936,5731,2626,972,5231,1831,1608,3578,3291,1967,5319,4740,6484,6717,4855,842,2940,4672,1464,3852,601,4797,192,3905,4524,3250,3186,6021,6516,5600,4136,2694,6452,517,4705,166,2654,513,1026,3372,4073,6392,3142,3900,6292,6329,5677,5997,5148,44,5810,3980,6364,6100,3599,2687,1010,22,5573,3451,1648,1398,3385,5792,2443,6343,4043,4292,4846,361,2658,6635,1778,6857,5485,2341,2734,1846,805,6426,1412,3062,4745,2025,2609,5806,2141,5173,11,973,778,4945,4461,1279,6600,273,1425,1532,5655,3771,299,1697,5577,1448,3586,4173,6243,2661,4076,5553,6431,523,2848,3126,2335,3929,4737,5885,385,1316,3788,1764,5364,2743,6804,2445,5963,4022,3316,1398,1494,5116,3338,2356,5576,2635,1545,3067,2994,3667,5162,3822,181,3897,2975,2888,1048,6978,4306,5791,5993,3003,6745,6604,386,6351,6847,517,376,3642,5913,2789,5323,292,396,1193,3780,5487,5122,781,1996,3052,5598,1644,6488,1465,1917,1074,3992,6911,2950,4932,6533,603,3377,4574,1365,5987,2895,6869,5871,1914,2008,5399,4985,3320,674,94,6328,5751,240,5220,1552,2344,827,4098,5277,6978,1863,225,2614,1099,1779,1473,1873,2325,3047,1485,433,1368,5790,6061,5407,4408,4907,2125,415,4866,5262,1367,790,4502,6653,2589,3746,2830,5175,4196,6430,6983,1508,6427,2051,3745,1452,4795,1451,5789,3703,2892,2597,4496,3332,6003,6525,4444,3351,2290,60,5806,5777,339,2966,6155,6408,6586,6679,3897,5872,3152,6220,6310,5858,6733,4548,5127,4574,4480,4570,1973,1215,4165,748,3913,6779,5609,2432,3191,1877,536,4902,6366,4991,3000,2178,3422,6913,3107,6664,4433,5636,1228,1370,1265,1264,924,2828,1388,948,4857,2343,4226,3408,5682,5126,134,1369,232,808,3029,4048,1816,200,382,3427,3654,2173,538,4757,6737,1077,4266,677,4653,2800,3187,5583,5138,2147,4199,5489,3642,6184,783,2220,1604,1452,1517,4363,6218,4498,4951,5319,377,4525,3957,6401,1662,6236,5080,6913,4773,1109,4122,352,2786,3975,574,3995,1099,4102,3660,2564,5081,2999,3425,5213,4172,1071,5291,6394,2278,4150,4950,3605,2665,2566,1686,399,178,2351,5487,4744,5043,2101,5287,6437,2580,891,5525,1252,2495,585,832,2553,6914,1515,5969,4372,1212,3585,133,3343,4002,6787,6258,3105,6215,1681,2770,4235,2868,6321,1958,4018,6906,5568,3218,3546,4737,1358,3058,3406,910,819,1142,6751,2135,3671,5825,3860,1735,1244,4138,5876,4356,2331,1955,4185,1221,6370,4857,910,4006,6108,1721,587,3474,6457,3738,1837,2741,776,221,308,4100,3856,3289,3244,6081,5942,553,5601,219,2378,3303,2377,10,6039,1584,6070,1884,6733,280,6506,4924,1870,158,1350,5939,437,2789,998,3209,1333,3111,4508,533,3002,1085,1793,920,1843,4398,5570,3281,6024,1608,4825,4046,4322,4601,4602,4926,731,3328,404,3959,6606,3317,2034,5645,3373,3795,441,4469,5474,3792,4558,1282,1371,1345,5985,6808,4794,1842,3645,4026,178,4362,4988,3483,5736,6464,6953,521,178,6617,2861,2130,2748,6872,3530,5308,2638,3636,4677,1029,3613,4990,6518,215,4078,2938,4733,63,4138,5041,4563,2399,4045,265,6715,4634,6351,4285,2253,5532,1255,5559,5796,5352,1142,4551,283,5994,6948,6461,2860,6643,4294,5712,6600,1729,4444,27,2097,4392,2827,2962,646,697,5189,2240,2535,5896,171,1570,2314,1567,3252,1444,790,556,930,1342,1841,2438,2353,3503,327,2115,6966,2068,6291,1277,5514,4684,2285,533,5665,4888,871,4884,6566,1376,3114,3178,6445,3233,4896,3691,3661,4858,2878,5602,1929,138,1214,3821,4973,4834,4919,6538,6030,5553,2882,5922,536,1188,6266,4283,4010,4541,6161,874,4315,5949,3332,2081,5482,1773,3842,5122,5716,4089,5218,1452,6593,4156,1735,4734,6204,3289,4654,2770,547,1194,4016,6674,3376,2609,604,331,4966,2511,3382,5310,523,127,1533,1411,31,5041,3993,6478,4906,3465,6965,846,4120,3758,1677,2896,798,5008,1696,1662,5695,6620,853,711,1786,1731,3162,5646,2220,1382,2267,1133,874,6037,5795,4470,1473,2831,6756,4708,1449,5065,5354,1600,2019,864,2745,6069,2764,5148,4841,4779,3500,821,3591,3634,6716,5694,3116,6935,4999,6262,6986,723,6254,4263,3517,3740,5959,4802,5544,4398,5329,1498,3846,1116,4330,6750,5829,1139,1099,802,4554,2842,5628,98,359,3410,2206,5046,5088,3129,4147,218,3001,2477,832,6420,1817,6394,3069,6138,4666,4140,1600,3325,5968,3731,1998,2729,1622,2108,1268,6561,3502,785,2635,1867,231,1256,5605,1356,2844,1200,2813,3705,3069,3906,4104,6923,316,6833,5370,4082,2909,941,2565,4858,6626,4369,3871,3786,3527,2076,1405,985,4898,6226,5555,5825,5514,2448,5372,1697,1437,5860,2622,3037,2306,3480,382,2179,1366,1203,4259,5276,4547,3746,4331,4672,6633,4505,6282,6598,3671,133,1353,5765,3784,5932,4886,782,4384,3097,1755,1752,2751,2668,5025,1802,1454,28,1454,1742,2754,5665,4221,413,611,3873,2828,6622,6773,5988,4517,5477,6456,6593,1361,3622,1114,3747,1971,3710,4919,1082,5766,5812,798,3544,3028,4050,3656,1309,1212,5291,2078,1847,6619,5291,6921,6318,4995,2991,1862,542,5520,2692,6297,2131,6490,6264,6145,1634,4432,2236,6318,6265,932,5703,3610,6439,5206,4622,2110,3069,5545,4762,1913,1771,21,2379,2228,527,2857,2555,3766,4785,6766,4313,591,4375,635,2025,2972,3713,1616,6708,5712,398,605,2816,2548,3802,5030,4724,4077,4409,2191,4013,6578,323,4320,2096,1181,6350,408,3182,5580,4431,591,3168,5629,4183,6930,6619,2851,6003,6971,6171,835,4313,3684,1692,5839,3534,450,427,485,6622,5148,2196,335,4954,3863,6563,1501,6514,6598,2562,3311,2848,1805,670,2669,307,1063,344,6605,353,1374,285,250,2185,1519,2670,6304,3864,4258,2905,6979,5197,475,360,6764,867,4633,6719,3491,6389,6347,6387,3625,692,2993,5599,3911,6742,3135,5082,5587,5886,2948,2860,1024,5381,1704,2082,2379,6188,5918,70,2587,998,453,5943,278,5386,1290,2567,5018,1221,1979,3553,178,993,2713,557,6734,6481,3317,3583,848,5036,5611,4834,4255,4065,524,6944,5747,3017,3651,4133,3286,3378,1675,21,6723,3863,143,1654,5175,5612,6551,2957,1347,4831,1460,3603,4659,3560,3639,1635,5703,5488,2308,2655,5472,1071,2159,2898,6436,3675,401,3542,6171,1432,5277,6095,4102,3042,3823,2946,6986,2802,3425,6258,6944,6010,3331,4674,756,3370,6434,3483,1579,4923,4106,2989,839,4931,6416,2976,289,5616,5992,3985,6079,6231,4130,6431,6106,2541,1387,6961,3463,3861,963,200,1730,1844,5728,6326,3060,609,5496,6386,6046,4796,6210,3591,5449,1288,6127,5512,1005,605,6361,1838,2614,2997,4051,2995,1100,5743,3738,3089,5790,6998,5252,1471,4819,225,323,3052,4603,2333,3146,4225,877,1153,4461,5544,1689,1473,4369,5187,5188,4677,1555,5561,610,4521,5634,3593,1388,6445,2813,4492,2708,4672,3140,83,2866,6816,754,1197,404,4104,1679,1380,5671,4054,1746,986,6637,5471,4256,4075,494,175,19,5464,1339,6146,4777,544,1294,1839,864,227,2017,1153,5619,6162,3682,5120,4301,2066,2778,6823,3765,1306,5658,2558,676,5078,6870,3729,715,2477,4456,979,4802,2008,4620,2938,1693,4327,1385,333,4822,5012,1849,4142,893,5907,2187,1294,951,6297,4236,3877,865,1791,4645,4524,5148,2251,6986,2116,3104,3926,6601,6669,6312,331,6700,5188,1855,5438,5570,3454,1318,5564,6494,4390,796,3724,4196,5217,4788,2469,6817,5878,6540,1533,4539,6820,699,1887,5775,5622,5966,1305,1810,688,5772,4074,3033,6055,5095,2415,2887,4160,6302,5609,1033,2889,2127,6976,3529,5081,6162,6216,5878,916,6555,2263,5450,5791,348,6733,569,576,5686,4767,4089,49,4044,2129,4954,3690,495,4579,1811,2281,6033,2815,4166,4897,971,1785,4557,6593,4615,6786,5343,6987,4083,5709,4259,5651,3273,3276,1790,3196,1585,3914,1864,6100,1107,3176,488,6774,4340,3909,6379,1109,6266,635,2711,1107,1483,3966,1816,4062,4276,3775,6224,4219,1980,3323,2353,3294,6353,2192,5460,2367,6255,733,3121,5218,3825,1871,6989,6397,1574,2746,2080,4673,229,4208,3770,2939,126,3355,4787,6751,95,4023,4459,6518,1377,806,1349,6039,5642,3916,4821,3809,4143,2682,6004,2288,3166,2204,62,3188,1270,2590,3484,5959,148,6717,3770,621,638,4577,212,5122,2819,6097,2004,6497,6918,6827,3455,2568,196,2889,3423,829,1163,2810,2128,788,5947,6134,560,830,3368,5708,4330,3729,491,4375,4850,3859,2185,6251,5603,4004,1116,6369,5557,5286,4186,1815,6906,5882,1383,4601,3109,6671,3696,2973,5012,6447,2825,1216,1997,2212,2638,898,2061,5917,2963,6689,4591,5273,1855,6160,6670,1821,5077,5963,4318,3055,6475,6141,541,1944,2092,5761,6025,6666,3856,1531,3966,1758,1949,4997,2094,3284,1559,4988,3944,3764,2191,6559,5353,3188,538,2159,1174,760,809,1792,230,4619,6947,5571,5723,3840,6434,1845,3225,2949,398,3677,5937,3033,3372,1783,4940,5793,4041,2900,6673,5619,1750,603,2282,6736,4566,818,543,3872,409,4654,2623,3891,2726,6409,1716,6258,5952,6195,4103,2826,3268,1860,3404,359,6583,5772,6578]) == []