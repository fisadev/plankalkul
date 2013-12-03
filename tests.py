# coding: utf-8
from unittest import TestCase
from plankalkul import guess


class TestPlankalkul(TestCase):
    def test_examples_from_document(self):
        self.assertEquals(guess('th jh qc qd qs', 'qh kh ah 2s 6s'), 'straight-flush')
        self.assertEquals(guess('2h 2s 3h 3s 3c', '2d 3d 6c 9c th'), 'four-of-a-kind')
        self.assertEquals(guess('2h 2s 3h 3s 3c', '2d 9c 3d 6c th'), 'full-house')
        self.assertEquals(guess('2h ad 5h ac 7h', 'ah 6h 9h 4h 3c'), 'flush')
        self.assertEquals(guess('ac 2d 9c 3s kd', '5s 4d ks as 4c'), 'straight')
        self.assertEquals(guess('ks ah 2h 3c 4h', 'kc 2c tc 2d as'), 'three-of-a-kind')
        self.assertEquals(guess('ah 2c 9s ad 3c', 'qh ks js jd kd'), 'two-pairs')
        self.assertEquals(guess('6c 9c 8c 2d 7c', '2h tc 4c 9s ah'), 'one-pair')
        self.assertEquals(guess('3d 5s 2h qd td', '6s kh 9h ad qh'), 'highest-card')
