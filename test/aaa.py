# Copyright 2021 Yan Yan
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

STR = """
BWG 0.0008761882781982422
BWG 0.0008311271667480469
BWG 0.002079486846923828
BWG 0.002329587936401367
BWG 0.0025458335876464844
BWG 0.0026700496673583984
BWG 0.002583742141723633
BWG 0.0025262832641601562
BWG 0.003481149673461914
BWG 0.003238201141357422
BWG 0.005095958709716797
BWG 0.0037899017333984375
BWG 0.003931283950805664
BWG 0.003300189971923828
"""
"""
0.003921985626220703
0.0049707889556884766
0.0052530765533447266
0.0060312747955322266
0.0036766529083251953
0.00421142578125

0.002129793167114258
0.0023038387298583984
0.0013151168823242188
0.0015285015106201172
0.0008392333984375
0.0008127689361572266
0.0002486705780029297
0.00030994415283203125
"""

STR1 = """
SUBM 0.0005137920379638672
F 0.0012662410736083984
F 0.0016875267028808594
REGU 0.0009055137634277344
M 0.0009114742279052734
SUBM 0.00037789344787597656
F 0.0020329952239990234
F 0.001947641372680664
REGU 0.0009374618530273438
M 0.00045609474182128906
SUBM 0.0009856224060058594
F 0.0009992122650146484
F 0.0010600090026855469
REGU 0.0006346702575683594
M 0.0004057884216308594
SUBM 0.0006394386291503906
F 0.0008478164672851562
F 0.0008838176727294922
REGU 0.0007183551788330078
M 0.00025177001953125
SUBM 0.0009539127349853516
F 0.0009481906890869141
F 0.0010502338409423828
REGU 0.0007147789001464844
M 0.000274658203125
SUBM 0.0007004737854003906
F 0.0009715557098388672
F 0.0012331008911132812
REGU 0.0008800029754638672
M 0.0002167224884033203
SUBM 0.00045108795166015625
F 0.0006735324859619141
F 0.0008375644683837891
"""
STR2 = """
F Turing_f16f16f16f16f16tnt_m32n64k32m32n32k16A0T1688_NS00_C3_01LLL_1 0.0007038116455078125
F Turing_f16f16f16f16f16tnt_m32n64k32m32n32k16A1T1688_NS00_C3_01LLL_1 0.0007627010345458984
F Turing_f16f16f16f16f16tnt_m64n128k32m32n64k32A1T1688_NS00_C3_01LLL_1 0.0007650852203369141
F Turing_f16f16f16f16f16tnt_m64n128k32m32n64k32A1T1688_NS00_C3_01LLL_1 0.0008864402770996094
F Turing_f16f16f16f16f16tnt_m64n128k32m32n64k32A1T1688_NS00_C3_01LLL_1 0.0004017353057861328
F Turing_f16f16f16f16f16tnt_m32n128k64m32n32k32A1T1688_NS00_C3_01LLL_1 0.0006165504455566406
F Turing_f16f16f16f16f16tnt_m64n64k32m32n32k32A1T1688_NS00_C3_01LLL_1 0.0005872249603271484
F Turing_f16f16f16f16f16tnt_m64n64k32m32n32k32A1T1688_NS00_C3_01LLL_1 0.0006289482116699219
F Turing_f16f16f16f16f16tnt_m32n64k32m32n32k16A1T1688_NS00_C3_01LLL_1 0.0002968311309814453
F Turing_f16f16f16f16f16tnt_m64n64k32m32n32k32A1T1688_NS00_C3_01LLL_1 0.0003299713134765625
F Turing_f16f16f16f16f16tnt_m64n128k64m32n64k32A1T1688_NS00_C3_01LLL_1 0.0002288818359375
F Turing_f16f16f16f16f16tnt_m32n64k32m32n32k16A1T1688_NS00_C3_01LLL_1 0.0002830028533935547
F Turing_f16f16f16f16f16tnt_m32n64k32m32n32k16A1T1688_NS00_C3_01LLL_1 0.0001780986785888672
F Turing_f16f16f16f16f16tnt_m32n64k32m32n32k16A1T1688_NS00_C3_01LLL_1 0.0003058910369873047
"""
def _handle_lines(s: str):
    arr = s.split(" ")
    return (arr[0], float(arr[-1]))
from cumm.gemm.codeops import group_by
def print_str(s: str):

    nums = list(map(_handle_lines, s.strip().split("\n")))
    num_dict = group_by(lambda x: x[0], nums)
    num_dict_ = {k: sum([vv[1] for vv in v]) for k, v in num_dict.items()}
    print(num_dict_)

print_str(STR1)
print_str(STR2)