# Tests for conjunction/declination encoding/decoding
#
# Copyright (c) 2018 Tatu Ylonen.  See https://ylonen.org

import unittest
from wiktfinnish import encode_paradigm, decode_paradigm

class TestStem(unittest.TestCase):

    def test_enc1(self):
        args = {"template_name": "fi-decl-valo", "1": "val", "2": "", "3": "", "4": "o", "5": "a"}
        stem, e = encode_paradigm(args)
        assert e == "NvaloG-Ho"
        assert stem == "val"
        d = decode_paradigm(stem, e)
        print("decoded", d)
        assert d["template_name"] == "fi-decl-valo"
        assert d["1"] == "val"
        assert d.get("2", "") == ""
        assert d.get("3", "") == ""
        assert d.get("4", "") == "o"
        assert d.get("5", "") == "a"

    def test_enc2(self):
        args = {"template_name": "fi-decl-valo",
                "1": "lä", "2": "mp", "3": "mm", "4": "ö", "5": "ä"}
        stem, e = encode_paradigm(args)
        self.assertEqual(e, "NvaloGp-mHö")
        assert stem == "läm"
        d = decode_paradigm(stem, e)
        print("decoded", d)
        assert d["template_name"] == "fi-decl-valo"
        assert d["1"] == "läm"
        assert d.get("2", "") == "p"
        assert d.get("3", "") == "m"
        assert d.get("4", "") == "ö"
        assert d.get("5", "") == "ä"

    def test_enc3(self):
        args = {"template_name": "fi-decl-palvelu", "1": "palvelu", "2": "a"}
        stem, e = encode_paradigm(args)
        self.assertEqual(e, "Npalvelu")
        assert stem == "palvelu"
        d = decode_paradigm(stem, e)
        print("decoded", d)
        assert d["template_name"] == "fi-decl-palvelu"
        assert d["1"] == "palvelu"
        assert d["2"] == "a"

    def test_enc4(self):
        args = {"template_name": "fi-decl-parfait",
                "1": "parfait", "2": "a", "ill_sg_vowel": "e"}
        stem, e = encode_paradigm(args)
        self.assertEqual(e, "NparfaitJe")
        assert stem == "parfait"
        d = decode_paradigm(stem, e)
        print("decoded", d)
        assert d["template_name"] == "fi-decl-parfait"
        assert d["1"] == "parfait"
        assert d["2"] == "a"
        assert d["ill_sg_vowel"] == "e"

    def test_enc5(self):
        args = {"template_name": "fi-decl-vasen"}
        stem, e = encode_paradigm(args)
        self.assertEqual(e, "Nvasen")
        self.assertEqual(stem, "")
        d = decode_paradigm(stem, e, pos="adj")
        print("decoded", d)
        assert d["template_name"] == "fi-decl-vasen"
        assert d["pos"] == "adj"

    def test_enc6(self):
        args = {"template_name": "fi-decl-maa-dot",
                "1": "DNA", "2": "a", "3": "a"}
        stem, e = encode_paradigm(args)
        self.assertEqual(e, "Nmaa-dotFa")
        assert stem == "DNA"
        d = decode_paradigm(stem, e)
        print("decoded", d)
        assert d["template_name"] == "fi-decl-maa-dot"
        assert d["1"] == "DNA"
        assert d["2"] == "a"
        assert d["3"] == "a"

    def test_enc7(self):
        args = {"template_name": "fi-conj-saada", "1": "my", "2": "ä"}
        stem, e = encode_paradigm(args)
        self.assertEqual(e, "Vsaada")
        assert stem == "my"
        d = decode_paradigm(stem, e)
        print("decoded", d)
        assert d["template_name"] == "fi-conj-saada"
        assert d["1"] == "my"
        assert d["2"] == "ä"
