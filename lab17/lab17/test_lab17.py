from byu_pytest_utils import max_score, with_import


@max_score(4)
@with_import('lab17', 'cs_classes')
def test_cs_classes(cs_classes):
    assert cs_classes('Is it unreasonable to take CS111 in the summer?')
    assert cs_classes(
        'how do I become a TA for C S 111? That job sounds so fun!')
    assert not cs_classes('Can I take ECON101 as a CS major?')
    assert not cs_classes(
        'Should I do the lab lites or regular labs in EE16A?')
    assert cs_classes(
        'What are some good CS upper division courses? I was thinking about C S111R')


@max_score(4)
@with_import('lab17', 'roman_numerals')
def test_roman_numerals(roman_numerals):
    assert roman_numerals('Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?') == [
        'IIV', 'VI', 'IV']
    assert roman_numerals(
        'My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit') == ['I', 'II', 'IV']
    assert roman_numerals('I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5') == [
        'I', 'II', 'III', 'IV', 'V']
    assert roman_numerals("Let's play Civ VII") == ['VII']
    assert roman_numerals(
        'The U.S. Constitution was signed in the year MDCCLXXXVII') == ['MDCCLXXXVII']
    assert roman_numerals('i love vi so much more than emacs.') == []
    assert roman_numerals('she loves ALL editors equally.') == []


@max_score(4)
@with_import('lab17', 'match_time')
def test_match_time(match_time):
    assert match_time('At 05:24AM, I had sesame bagels with cream cheese before my coffee at 7:23.') == [
        '05:24AM', '7:23']
    assert match_time('At 23:59 I was sound asleep as the time turned to 00:00.') == [
        '23:59', '00:00']
    assert match_time('Mix water in a 1:2 ratio with chicken stock.') == []
    assert match_time('At 2:00 I pinged 127.0.0.1:80.') == ['2:00']
    assert match_time('These are nonsensical times: 05:64 and 70:23') == []


@max_score(4)
@with_import('lab17', 'area_codes')
def test_area_codes(area_codes):
    assert area_codes('(111) 111 1111, 1234567890 and 123 345 6789 should be matched.') == [
        '111', '123', '123']
    assert area_codes(
        "1234567890 should, but 54321 and 654 456 78901 should not match") == ['123']
    assert area_codes(
        '680-651-3924 is a valid phone number, as is (169) 657-5623') == ['680', '169']
    assert area_codes("no matches for 12 3456 7890 or 09876-54321") == []


@max_score(4)
@with_import('lab17', 'most_common_code')
def test_most_common_code(most_common_code):
    input_text = '(123) 000 1234 and 12454, 098-123-0941, 123 451 0951 and 410-501-3021 are all phone numbers.'
    assert most_common_code(input_text) == '123'

    numbers = '''(415) 352-3317
771 397 2227
270 091 7007
7406010391
415 862 7019
1077191228
(829) 431-8653
(829) 610-8954
490 743 0474
415 844 9898
1076509907
(829) 849-6734
458-610-5502
941 901 3203
490-993-4299
415-525-2035
270 596 3647
(740) 717-6269
7719829173
814-890-5732
7404927888
829 630 2417
(814) 546-6130
107 131 3712
(941) 954-6695
740-854-6617
4587998194
415-525-9604
270 280 6479
9414600216
740-585-9805
(844) 712-8375
527 753 2033
(479) 357-5519
1074868110
8298307449
270 761 1284
5274400002
458 745 4081
8297867944
458 880 3418
527 136 3175
4151548444
527 558 4917
527-661-5089
527 455 0132
(829) 969-0810
9669940168
(527) 202-4373
087 276 2508
829-659-3576
(527) 857-9299
740 284 5509
107-274-1715
941 229 8099
(490) 587-6820
(844) 647-6719
(479) 234-4932
(966) 182-4830
771 205 0590
5271503142
829 002 4964
2707026647
107 635 5116
(829) 258-8062
(740) 352-1571
829-081-9209
458 307 0216
(490) 075-4166
490-156-9376
9413449321
(844) 787-5368
829-399-6520
941-242-3115
740-232-7131
4156243361
8295368491
107 398 9170
(415) 601-9453
(490) 757-2241
(527) 118-6391
740-347-6181
2709873100
458-073-9874
4158934316
270 278 1087
415-659-4217
740 475 8199
(527) 949-9151
2706072739
415-538-0102
(270) 381-4952
490 014 8272
415 694 6272
740 759 8456
479 960 4131
479 067 7201
270 319 7348
490-054-4502
740-472-1922
941-223-8576
941-978-8201
941-537-0145
4583933221
458 050 4952
(740) 260-8195
9410914099
4151739512
2703937832
941-558-3222
458-850-3940
4158122961
490 276 1951
(814) 253-4989
270-316-9197
8449435317
5279366186
2702591059
(844) 947-0367
458-555-8945
941-540-0733
8295217900
8446394275
527 500 6892
4909413163
(829) 097-0155
(270) 300-0884
(527) 982-0335
2705577877
107-514-4444
4580888614
7402213659
4155982996
(490) 570-7684
107 178 5008
7717029788
4150061090
7719767672
(740) 717-0680
9410402295
(740) 801-4892
(490) 500-5529
7408121885
7404525771
941 105 1747
4158064421
941 802 5439
(829) 039-7781
829 978 0086
(527) 142-2823
7719124845
527-685-9381
1071156488
107 461 3101
9411982903
(490) 340-1021
941 462 1319
941-776-6351
5273736986
4155390857
107 370 1126
(829) 696-5271
4589683887
771-615-4053
(941) 135-3804
941 741 1771'''
    assert most_common_code(numbers) == '941'
