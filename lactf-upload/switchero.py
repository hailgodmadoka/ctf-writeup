from __future__ import print_function   # PEP 3105

from z3 import *
datax = "06050403020100077EFC3C78FBF4043E038730043D81709D4DA73D09F8A1514AFC028BA8B250490C4BFDF062921DD202A946BEAABE81E7889419BB850E0F0977FB493F3524B84E56479B62EB9D7A0B7FD1186E1430B13F01ED65D44D7EE150E6E7AB3D800467D3817A8C7173A380CE027348253009512C824E68705047370857B5141032EC34D73BB398DD7EE31E5E97FD4C0DB6FE448115914215AC6C7C40881BFC0D922B19AE0F8026767C6E670CFC27EF946DD3B85048A24D880D72666408DC484FC153047EACD8DF6124AD68257C081F91DE5D063B477158E642D71FED1E4825B8C1C3ED816CFF0218B6719F1603E03FAE926739A7E4CAB7106BAC08CF90A081F03109A14C003B68898FF13DF500498FDEB1BC424200CA84ACCE00597E00A40E11E80F6F70004E506220B47822009C2BA55DA9052A00490EDFB9D0C54D00C4F06CE041366C006E4A378EA64779000268332B63D2D8002E02B52FC45638011839081ADB143B00BBE12FB13A67F8002412ED14B008A100043BEF6A2E89B200D6240018D33C2C02345FFCD0AA113902E64E4B71C9070802272330091C331A0745D2A9212906180453920F2B34161F057CE90ADABF193B011E2F19352517120795D210C90B2A3203946319FAFF70C000DD9949A872B09A00ACAAA174E1824E00B98495410552AA00D5E31E8C2B8A6700D0E7D8C9ACBC4500F9D4B084C3193A001BC582A560198B00CD2A2A6C50C44E00E1865760C87374007FB3BA6B53161301EFDEDB7F240D0F00761EDEA908F6AD00E382CF6808549F001D802B31FCF51400FE2432C4146F1000C5378B5DAD5BB8000D998C8417CEED00C4BC11DF13DCCC009B55A076672D0C02F72175EA641B0A0282BE90D9241D3900A83CD79D71007500372AA8B2AD2EEF00601496400AF18E00A5673FFE2C9A33009D8765633071E000F0DC752A3D6E6E00F07382C154722E017F669BCDAD0848009563EA301280100138FCF1F1C798FA00D97BFEE60F400D014DB90800159E470095481338CF80F900AC5DCB7BFE0F2A00999BCE0F4B0B75005877B379FE6EBD0028361531240E200702BC3240F1AA7C00BB9583611F013D029E6FFE3478805300C87086E83D300201F8D808C73A0CF500BC759DA9F85EFF007E510E10123A040206D749D0192DE800144262DB312614020BA6FFB06313A900F9B27D13A18E8500EC18B006FA4F6F0034F08076E757000172728C8BB85A5A00821D083468191D01ACEAFA5607EE6D007800160CE861160013C3581A7AA6CC00E8131BB8833622018DD64503C2CA6500DCEC50601A1C030105192C97EC043701250B6C8BE4C94E00DDE1A5120DC455000EE420C4FCD4F000F3278B99C1B89B00F61A04045DC8CA0005BA8E89AF4105029510673D26B02C004336ACE7FF423E028760094E62F31900EC88A75A99D3F826".decode('hex')
# data = map(ord, data)
dataarr = []
from pwn import *
for i in range(0, len(datax), 8):
    dataarr.append(u64(datax[i:i+8]))

###########################################################################
# Rotating bits (tested with Python 2.7)
 
 
# max bits > 0 == width of the value in bits (e.g., int_16 -> 16)
 
# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
 
max_bits = 64  # For fun, try 2, 17 or other arbitrary (positive!) values
"""
aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
"""

"""
"""
import string
setring = string.printable
flag = ""
# for i in range(64):
for i in range(64):
    for z in setring:
        tebak = ord(z)
        coba = 0
        print(hex(dataarr[tebak]))
        v3 = rol(dataarr[tebak], 8, max_bits);
        print(hex(v3))

        v4 = v3 % 256
        print(i, flag + z)
        for j in range(v4):
            print('yet  ')
            print(hex(v3))
            v3 = rol(v3, 8, max_bits)
            print(hex(v3))
            print("compare", hex(v3%256), i)
            if(v3 % 256 == i):
                coba = 1
                break

        if(coba == 1):
            flag += z
            break  