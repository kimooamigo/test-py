import sys

# Ghosts Net
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
if PYTHON_VERSION != bytes([51, 46, 57]).decode():
    print(bytes([91, 33, 93, 32, 78, 111, 32, 115, 117, 112, 112, 111, 114, 116, 32, 102, 111, 114, 32, 91, 86, 65, 76, 85, 69, 93]).decode().replace(bytes([91, 86, 69, 82, 83, 73, 79, 78, 93]).decode(), sys.version.split(bytes([32]).decode())[0]))
    exit(0)

import marshal
exec(marshal.loads(b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00s\xce\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa0\x05e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa0\x07e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x03d\x06\x85\x02\x19\x00\xa1\x01Z\x08e\x08e\x03g\x00d\x07\xa2\x01\x83\x01\xa0\x04\xa1\x00k\x03r\xb4e\te\x03g\x00d\x08\xa2\x01\x83\x01\xa0\x04\xa1\x00\xa0\ne\x03g\x00d\t\xa2\x01\x83\x01\xa0\x04\xa1\x00e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa1\x02\x83\x01\x01\x00e\x0bd\x02\x83\x01\x01\x00d\x02d\x03l\x0cZ\x0ce\re\x0c\xa0\x0ed\n\xa1\x01\x83\x01\x01\x00d\x03S\x00)\x0bF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N\xe9.\x00\x00\x00\xe9 \x00\x00\x00\xe9\xff\xff\xff\xff)\x03\xe93\x00\x00\x00r\x02\x00\x00\x00\xe99\x00\x00\x00)\x1a\xe9[\x00\x00\x00\xe9!\x00\x00\x00\xe9]\x00\x00\x00r\x03\x00\x00\x00\xe9N\x00\x00\x00\xe9o\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x0b\x00\x00\x00r\x0f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00\xe9V\x00\x00\x00\xe9A\x00\x00\x00\xe9L\x00\x00\x00\xe9U\x00\x00\x00\xe9E\x00\x00\x00r\t\x00\x00\x00)\tr\x07\x00\x00\x00r\x12\x00\x00\x00r\x16\x00\x00\x00\xe9R\x00\x00\x00\xe9S\x00\x00\x00\xe9I\x00\x00\x00\xe9O\x00\x00\x00r\n\x00\x00\x00r\t\x00\x00\x00s9\x10\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00s\xce\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa0\x05e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa0\x07e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x03d\x06\x85\x02\x19\x00\xa1\x01Z\x08e\x08e\x03g\x00d\x07\xa2\x01\x83\x01\xa0\x04\xa1\x00k\x03r\xb4e\te\x03g\x00d\x08\xa2\x01\x83\x01\xa0\x04\xa1\x00\xa0\ne\x03g\x00d\t\xa2\x01\x83\x01\xa0\x04\xa1\x00e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa1\x02\x83\x01\x01\x00e\x0bd\x02\x83\x01\x01\x00d\x02d\x03l\x0cZ\x0ce\re\x0c\xa0\x0ed\n\xa1\x01\x83\x01\x01\x00d\x03S\x00)\x0bF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N\xe9.\x00\x00\x00\xe9 \x00\x00\x00\xe9\xff\xff\xff\xff)\x03\xe93\x00\x00\x00r\x02\x00\x00\x00\xe99\x00\x00\x00)\x1a\xe9[\x00\x00\x00\xe9!\x00\x00\x00\xe9]\x00\x00\x00r\x03\x00\x00\x00\xe9N\x00\x00\x00\xe9o\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x0b\x00\x00\x00r\x0f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00\xe9V\x00\x00\x00\xe9A\x00\x00\x00\xe9L\x00\x00\x00\xe9U\x00\x00\x00\xe9E\x00\x00\x00r\t\x00\x00\x00)\tr\x07\x00\x00\x00r\x12\x00\x00\x00r\x16\x00\x00\x00\xe9R\x00\x00\x00\xe9S\x00\x00\x00\xe9I\x00\x00\x00\xe9O\x00\x00\x00r\n\x00\x00\x00r\t\x00\x00\x00s\xbc\r\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00@\x00\x00\x00s&\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01e\x02d\x03d\x04\x84\x00d\x05e\x03\x83\x02\x83\x01\x01\x00d\x06S\x00)\x07F\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00C\x00\x00\x00sD\x00\x00\x00|\x01t\x00d\x01d\x02\x84\x00t\x01g\x00\x83\x01\xa0\x02\xa1\x00g\x00d\x03\xa2\x01t\x03\x83\x03\x83\x01|\x00\x83\x01t\x01g\x00d\x04\xa2\x01\x83\x01\xa0\x02\xa1\x00t\x01g\x00d\x05\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x03S\x00)\x06Nc\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00\xa9\x00r\x02\x00\x00\x00)\x02\xda\x02.0Z\x03___\xa9\x01\xda\x01_r\x02\x00\x00\x00\xda\x06string\xda\n<listcomp>\x08\x00\x00\x00\xf3\x00\x00\x00\x00z.<lambda>.<locals>.<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x05\x00\x00\x00r\x02\x00\x00\x00r\x04\x00\x00\x00r\x06\x00\x00\x00\xda\x08<lambda>\x08\x00\x00\x00r\x08\x00\x00\x00z\x1a<lambda>.<locals>.<lambda>)\x1d\xe9_\x00\x00\x00r\r\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\r\x00\x00\x00r\r\x00\x00\x00\xe9(\x00\x00\x00\xe9"\x00\x00\x00\xe9z\x00\x00\x00\xe9l\x00\x00\x00r\x0e\x00\x00\x00\xe9b\x00\x00\x00r\x15\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00\xe9d\x00\x00\x00\xe9e\x00\x00\x00\xe9c\x00\x00\x00r\x11\x00\x00\x00r\x0f\x00\x00\x00r\x10\x00\x00\x00r\x12\x00\x00\x00r\x1c\x00\x00\x00\xe9s\x00\x00\x00r\x1e\x00\x00\x00)\x08\xe9<\x00\x00\x00\xe9M\x00\x00\x00\xe9R\x00\x00\x00\xe9G\x00\x00\x00\xe9H\x00\x00\x00\xe9O\x00\x00\x00\xe9S\x00\x00\x00\xe9T\x00\x00\x00)\x04r\x1c\x00\x00\x00\xe9x\x00\x00\x00r\x1c\x00\x00\x00r\x1d\x00\x00\x00)\x04\xda\x04eval\xda\x05bytes\xda\x06decode\xda\x03chr)\x02Z\x05_____Z\x06______r\x02\x00\x00\x00r\x02\x00\x00\x00r\x06\x00\x00\x00r\x0c\x00\x00\x00\x08\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00sk\n\x00\x00x\x9cU\x98\x0b[\x13\xc9\x12\x86\xff\n\x1bQ\x92\x15\xb0{f2\xe9VXt\x81\x05Dt\x11\x11\xd0pt\xae,\x88\xe1\xae\xe1\xfa\xdbO\xbd]\xed\xb3\xe7\xf8\x98!\xd3\xd3\x97\xaa\xaf\xbe\xfa\xaa&\xcd\xb8\xa9\xba\xdd\xe3\xe2{Y\x17\x13_\xf87\xad\x7f\xbeL<\x8f_\xba\xcd\x8f\xe2\xf8\xff\xe6L\xf3?>\x9f=:9\x1cu?\x7f\xe9\xca\xf7\xdeD{r\xce\xe8\xc4\xe1H\xfe\xec\xf7z\xdd\xa9\xa9\xe9\xcf\xbe?=\xc1\xc7\x9ap\xf1r\xb1\t\x17\xcb%\xe3\x92\xeb\x0c>\x99\x99\x9eH\x19L\x98c\\\\\xe7\x9d\x0eg\xb2(\xcb\x194\\\xe4\xce\xfb_{\xfd\xcf\xd6Y|hm?\\\xf6\xa7\xab\x7f\xce\xc5\x9e\xe0Qo\xba3\xb7\xf1~e\xf5\xdd\xd6\x87\xcet\xa7\x11\x08:\xf2\xa8\x9c\x1a\x0f\xc7\xbe\xda\xfe8\x1c\x9brg8\xb6\xa9\x97K6\x1c\xb7\xcdS\x19\xea_\xcb\xd3\xfep\xdc\xd4\xc3qU\xc8\xc57\xc3\xb1\x93)\xcet\x87\xe3\xc2\xcc\r\xc7e.\xf3\xdc\xef\xdc\xb1\x93\xdc4_\x935\x99.3m\xbe\xce\xbel$\xcf\xadLjeR-\x03\xed\xe0A\x96\xcaF\x8d\x95\x8f\xac*\x9a\x15\xb9\xe4\xa9,\x94\xd1\xaa\xbe\x7f`\x92\xcc)\xcf\xb0JV\r\xa6\xa7e#\x99\xda\x8ay\x85lX\xca\xd2\xb2\xb8\x12c\xe4\xa8A+\xd3j\xec\xf6\'2,\xdf\\\xf1L\x0fo\x9a\xb7\xf2\xa5\xe5\xd9pJ6\xe2\x0cY\xda\xcaH\xe9\xf4o\x9b\xc8\xbcZ\xf6\xb5\xed\xac\x1e\x10\xcc\x97\xf3\x1b\xa7\xbb\xd5\xec\x9d\xc8\xc1\xa9\xfd\xf8Y\xbe\xd6\xbfqQ\x8f\x81\x00\xa78\xacM\xf5\xe3\x03X\xbf?\x9f\x91\xdb\n\xcc&\xe7\x00v~\t\xc3\xe4#[W\xe6\x91\\\x06\xecY\x0f/u^\xd3\x17\xe8\x8a\x01\xa8\x17b\xa3\xeb\xbf\xe9\xc8`\xea\x1f_{\xc6\x17\xaf\x15\xfeJ\xdc7Y\xf4\xaax/S\x8a= \x02\x87\x0fr78\xdb\x92\x89\xae3\xf7\xf6\x05`\xca#6\x17\xfb\xa7\x96\xd4\xcf\xa6y#\xfb\xb5`\x7f/#E\xfc4\xc0q\xe7\xd4]\xef\x7f\xc8E&\xbb\xe4\x90\xe7I\xf4,\xbd\x91\xa5r\xe3\x0bL\xe7s\xd3\xd1S\x8a\x01\xdf\x18\xc7G\xdb\xac\xcd\xcb\x12;<\x97\'\xb5\xc2\t\xb4\x1e\xac\x89\xdd@IS\xd7Gr\xd3\x07/\xa7vphI\x94\x81\xa0T\x90\xeaZ\x8e\xf5\t\x01+d\xc3\xb6?3\xbc\\\x95\xa1\xaa\x0c\x81\x1d\x17N\x82{>s\x1dN\x1c;\xf6\xcf\xfa\xc3\xf3\xc3\xad\xeby+\x88\xd5\xb9\xb2\x90m+\xf7J\xb6\x82\\\xf9\x1a,\x14(\x1a\xffN\x8d\xf2\x81#\xd0\xab\xcegqVndI\xed\xf7\xe5\x06\xbc0/\x9d_\xfe\x0cey\xb6\xfd\x1c\x0c,\xa7\x8bg\x7f\xc1\xaf\x95d\xf1F\xb3\xc8U\xca7\x97\xfc\xb6<)\xb3\xfd\x0c\x81\xae\r\xbc\x96\x0f\x88:\x80\x9a\xc15Bz\xef\xf9&\xfe5\x00\x95H\x0e\xd6NI\xe6\x92HUO \xe7\xefcR\xa5\x8a@0\x8d\xbc\xac\xe76\xe6\xfe\x04#\xf9\x9e~\x0f\xcbG\xca\xf7\x12F\x97\x0b2\x97\xb4\xf5\xfe\x82T;q\x18T\xa5\xdb\xca)o\xff\x96=\xab\xb8@\x06\xaa\xec\x12\x9f\xaf?\x91\xff?Ve\x07\xcf\x02\xcfy\x8e\xe7\x89QL\xf1\x12\x8f}\xf4\xda\xe5K\xec\xe0>\xbdP\xc3\xca\xa6\x84\x01\x97\n[\xeb\x969-\x0b\x1e\x80@}\xfaZ\x1c\x1a\x1c\xfcJ\xba\xc7\xeb\xbbK\xbb\x93\xec0\xb93\xa3;\x10\n@*\x92\x97\xcb\xb2\x8d\xc9\xd3\xbf\xafN7\x9e\xf6\x0e"g\x92\x9fA\xab\xa6tf\xdd\x8cH\xd01\x90\xc8\xfad_Q\xac\x93\x15\xd5\x8b\xaa:\xc3\x947\xa0/\x9b%O6P\x8a:\x88\xcd\x1f 2\xa1\xcaWW\x98d!a\xb9\x86\xe79\xfbw\xcf\xcc\xa2\x8c\xdb\xcd\x8f\x1aE\xef\xb0\xd5\xde\x10\xb8RS\x14\x01 !]\x0e\x80\xcd\xf0\xfc\x84D\x96EQ\xc1\x1c\xe9\x9bLh\xe2\x18\x14\xa4\xafaCbmP\x9c\xad\xa8\x97\xc5\x852R\x023\\x\xb4)\x8f\x93\x88S\xa3\xa0\x17\xfe;\xc9r\xa4t\xaa0\x193%\x86\xb6\x7f\xd3Sq4D\x12,H\x8d\x82\xf4\xec?_V\xce[\xbf\xd9\xf9K%\xach\xbe1%\r\x87M\x85p\x0bi\xbe\xc9\xa5\xc85t\x84\xa22\xea\'\xa7\x18\x83\xfew\x87\xa3}\r>\xfeA\x80\x16v\x94\xab\x1d4[\xb02\xf6\x90\xf9@\x9bG\x1f\xabc\xe0\xbd\xd8S\xa6\x91\xfb\xb0\x19\x8f\xdbA\xef\x12\x10:\x8f4O\xad\xa16\xe8Y\x12\xdc\xd1\xdakMh\xebg\x01\x11\x00d\xdfv\x13\xb4\x9fa\x06\xb8\xdb\x97\x9b\x85.7\xd1\xec\x82\x10\x9b\xce\x98\x98\xbdSo\xd0"6h\xa3\xa06xf\x1eb\x85\xa8\xcbIu\x089t\x83W\xa8\xcc\xc3\x15\xa90\x8a\x9c\xac\xce\x8e\xc2\xd3sN\xca5\xb2&\xebP /\x9e\xe8\x89\x88\x973?\x80zY]%\xf7\x9dy\x16\x0b\x8b\xb1[\xcb\x1a4\x02&\x828\xc5\xe9K\xca\x10\x14\x19\x15\xb4Y\xf7J\xad\xf4\xcdg%\x16u\x12=n\xec\xbaK\xca\x9d\xc7\x8c\x80\x7fs\xb8G\x05@\x87? \x8d\x8b\xc7 \x90\xdd\x12C\x82\xb9\xa4\xfb\xe0\xa9\xf7/^RCw9\xfb\x8cm\x9d\xca\n@c\x11\xf2\xdc\xda\xdb\xa7*\xd6\x15\x99\xea?\xc8I\r1\xcc,\x91W;\x9bBNqmqD\t\xfb\r\xa6\xcf\xf6\xf64.u\xc8I&\x96\x95\xeeNj\x04\xda\x0e\xa2v\x94\xf1\xef`i8$\x1e\x07\xef\x1f\xa2\xf83\xa3\x85\xaf\xdf8\xe3\xc5\xfe9\xe6.\x1fk\xc6\x14\x99\x06\xadr+\x12\xce\xb6Tu&\xda\xbe\xb8\x81w{\xb8\xa8i\x02\xb5\xa8\x96\xdc\x87\x02\x95iTe\xe7Wk\xe8\x82:ks4\xcc\x02C\xd5\xc3\xe2\xfd\xe5\x9er\xcf\xba\xb7\x9a\xd8\x85\xf9q\xa5t%\xd9(\x84\xb6\xdeP\x9d\xae\xec\x8e\xeeL\xa7\x80`\xd7\xf02\xf9\x08\t\x9e"\xbc]e]e,V\xd3\xa8\xe4\x1b\xc4m\xf5\xef\x15\xcdh\xa01ew\x01\x88\x13\x8dCS\xcc\x1e\x10\xc7Cb6\x93<Q/i~\xe8\x9d\xaa,\x14\x9f\xb1I\x95NM_\x0b\x82\r\xfa\xda\x1e\xa9b1b\xd8L\xaadX\x8e\xd0\xb4\xd9\x84\xf6^\x86\xfeJ\xe0\xbe\xdc\x1a\xadf*\x9f-)\xc4\x82 3\xa9\xf6b\xad_Eg\xef\'\x95|>#\xaf\x9b\xf9\xd8$\xe1\xff\xe0\x1e\x01m{[\xba(\x18gv\xb5\xd3\x08\xbe\xe4*^\x086\xf5HN~\x175\x95h\'\x8fUCL\xccF\x82\x86\x16\xd9r\x1f\xe0\xb6u\x93\xe0z\xfa\x05_\x0f\xdc{\xc5\xac\xad\xfeP\x0c\x90&\xa9E\x91qth\xb8J\xdb\x08J(\x7f\x10\x1ad-\xc1\n\xa2\x84\xfbe\xb9\xf3U\xf9\x86\xb0\x15x\xcadK_E\x9c\x89h\xe8d\t\x1f\xc5\x96\x82G\xe3g\x7f\xb5\xacQ=\x98\x08\x151\xc4#\xfeu\xfb\xeaW\xab\xa5\xb5\x15\xc7A\xc7P4\x18h\xfd\xb1\xca\x0c\tZW\x0b\xa8\x03\x11\xa4\xf4\xba#\xb5\xb1L\xff"\xc1\x08\xe5\x06\x84\xbcEr\\\xd5\xb9\xbcUEuA\xbdB\xfa.)3L\xb5\xbez\xa6\x84\'x\xdehS\xd1f\x8f\x08J\x1e\xc09\xa77H\xee\x00\xe9\xc7F\xfa\xba\xa1 \xe4\xc7\x94\xbf\x10!\x8cD|\xcck\xda\x83Cu\x81Z\xe8\x93\xe5X\xa4\xd2\x98\x8a\xe9K\xad,\x01\xdd\x96\x08w\xe9t\x06\x9b\x94\xf5\x9e\x16\x12\xd0u\xe1\xf9\t\x98-\xd2\x16:\x8d\x1f\xc8Y\xbf\xa5o\x1a\xc6\xc4~\xc2\xc6\x8c\xeeo\x9d@\xcbS\xc0\xd4\x8e\x90\xd4\x0f\xc5\xcc\xa9w\xa1\xc5K4<\x80G\xaa\xd7Qn\x8a\xc1\xd3\xeb+\xa5\r\xcd\x13E\x8b\xe0\x18SG\x12\xe6\x9a6\xc6\x1cOh5\x10q\x1a\xa9)\xa1\x8f\xcd\x7f\xc6\xde\xb0P\xc5\xad\xb8q\xc5\x1c\x97q\xf7c\xecl\x07J\xb5\x90P\x81n\x13\xb1\x14\xa7Z\xe3m\xb6>\xe9\xb1\xecOm\x9d\xacG\xe3\x9b\xd1\xb6\x96\x12\xd3\xbfQ\xa5\xa2\xc7!\x1b0\x1f\xe6\x91\x8e\xd6?\xe8\x97\xb2\x88\x1d\x84\x9dTO\x02\xab\x01\xdf\xf3\xa5\xea\xa7Q\x02\xd2[\x1c{\xa39\x14\xc0\xaf>i>\xb0\xa2i\xa6\x13\xae\x9b\xf3\x13\xba\r\x1dt\x93|\xc0\xda\x9e\xf2\xb9t\x0bJ\x1e\x98`\x92\xddb}\xf6L;\xd0\xa2P#ay\x88\xff &\xb4\xd5\xcaB\x05w\xd9\x96\xf6,MvYwc\x86\xa4O\xd0yZ\xcd\xbc\x0bHi\xe7`W\xc3E\xa7E\xb4\x8bt\x86T\x9c\x8b\xe5>#\x8fQ5\xd3|\x01\xfa\x1d\x04lR\x13\x1di\xa5p\x04F\xa0l\xf6?\xf3_\x17\x08-4I\xe6\x93\xa8:Hrk^\xa9\xb9\x8c\xb8\xe6d\x10\xbb \xa7\xf1\x0c\xbdUx\xcf+\xa9?\x14\x1e^M\x89"\x82\x15\xb8\xd4\x0e\x87.R\xdd\x1f\xb0\xc9\xa6V\xf7\xda+\x11\xebj\t$W\x9eA\xd9~\xe8S\xea\xf7\xdaF\x84B\xd94\xa7\xb1\xe8\x14\x1b\x9aUT\xd3\nF5\x8fY\x94\xde\x877)\rVi\x0b\xf7q\xac\xbaM\x16\xc2\x97\xa6\x8d\xfa\xe7\xdb\xb7\x0f\x1a\x812\xf6[XjB\xdf\xf4\x0f\x89z\x7f\xb05\x1c\xf9.V\x97:\x01\x1e\xb6\xa1.\xfe\'r\xbdTkP\x14\\\xb7\x91t\xe2 \x08\x14?\x15X\xe3\xfe\xa0\xe8\x15*\x1d\xe1M\xa6~\x98g\xe9J\xae/u\xa5{\xfe\x9c%\xf4Yu\xfe\x9d\x1d\xe3\xdb\x16g\x97\xe1%\x95\xc3\xab1\x87\xfesi\xe3\xd4Z\xa3\x18\ne\xfe\x99I7\x8a\xb4\xb3{\x91J\x99v\t\x15T \x0e`Y\x87\x8e\xf7\'t\xde\x81ff\xe7W\x98\xfb\x9ae\xc1\xb9$\xda\x9a\xbf\x8a\xc5\xb2\xf9\x96\xf1\xeeRn\x8e\xf4\xf5\xb0,N\xef\xb4\xb3\x00\x88\x12\xfay\xb7r1\xa7o\x03\xc4\x93\xccs\xee\t\xf2\xb8\xba\xfc\xfb\xa9\x06\xbaH>\xf1\xf4\xf6\x16\x8f+X\xc7k5\x91\x08\t\xde\x7f\xf9\x8dCOT\xd2(\x88\xa1\x9e\x98I*KC:e;\x9d\xd71\xa2VK\x1d\tc\xdd:{\x8fm\x14\x0b\xf7o\x9b\x12\xde\xe9\x9a\xb5\xc5\xf8\xb6\x055\xeb~\xc0\xe3\xeb\x05iq\xb1\xad\x0e\xb5(Z\x15\x7f\xbb\xa9\xda\xab\x86\x18,\xb6#\xcdX\x94\xda\x93}\xa4&\xcdt\xe5\xf8\x99\xa3\xa4?\x02\x1f\x94.\xbc\x06\xf5\xf5T[-|Y<=S\xbeC\x8d\xa2\x7f\x87m\xa3(3\x01\xf9]u\xaf\xedo\x03\xf0fu\x87\x10}S\xa5\x0c\x89\t,\xe1\xe7\x1d\xc2\x92\x1e\xe9\xe3s\x945\xfc\x82DD\xd3\xf9\xa5G*\xdaD\xbc\x8a}\xa1\xc9\xc6\xe3\x7f\xbd\x01\x12\x8c\xaa\xe5H\x1a\xd1\xf6.Ja\xab\xf4\xfdU\xf5y\x0f\x0b\x0e\x94\xf1\x05\xc6\x1d\xc0\xa8\xbd\xf8\xba\xe4~.+\x18\xa1\x07\xb1Q\xe4\xaa\x87?iY\x07\x9d\xb7\x9b\x8f0\x82\x9fa\xb2\xbb{\xdd\xa5i\xb3\x7f\xdf\xb0\x8b\xf8;C8\xaa\x1f\x7f\xc5\x8amM\xe1;$n>5]\x9d|?=<nz\xbd\xff\x02\xba\xda\xf1\xbeN)\x04\xda\x03foo\xda\x03bar\xda\x04exec\xda\x07compiler\x02\x00\x00\x00r\x02\x00\x00\x00r\x02\x00\x00\x00r\x06\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s\x06\x00\x00\x00\x04\x01\x04\x01\x08\x04)\x0f\xda\x03foo\xda\x03bar\xda\x03sys\xda\x05bytes\xda\x06decode\xda\x04join\xda\x07version\xda\x05splitZ\x0ePYTHON_VERSION\xda\x05print\xda\x07replace\xda\x04exit\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r)\x00\x00\x00r)\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x12\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x03B\x01\x14\x01>\x01\x08\x02\x08\x01)\x0f\xda\x03foo\xda\x03bar\xda\x03sys\xda\x05bytes\xda\x06decode\xda\x04join\xda\x07version\xda\x05splitZ\x0ePYTHON_VERSION\xda\x05print\xda\x07replace\xda\x04exit\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r)\x00\x00\x00r)\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x12\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x03B\x01\x14\x01>\x01\x08\x02\x08\x01'))