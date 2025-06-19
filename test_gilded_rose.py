# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_items_property_should_not_be_changed_on_account_of_goblin_attack(self):
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)
        self.assertEqual(type(gilded_rose.items), list)

    def test_quality_decreases_each_day(self):
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)
        foo = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, 4)
        self.assertEqual(foo.quality, 9)
        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, 3)
        self.assertEqual(foo.quality, 8)


    def test_quality_decreases_twice_as_fast_after_sellin_has_passed(self):
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        foo = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, 0)
        self.assertEqual(foo.quality, 9)

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, -1)
        self.assertEqual(foo.quality, 7)

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, -2)
        self.assertEqual(foo.quality, 5)


    def test_quality_never_becomes_negative(self):
        items = [Item("foo", 1, 2)]
        gilded_rose = GildedRose(items)
        foo = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, 0)
        self.assertEqual(foo.quality, 1)

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, -1)
        self.assertEqual(foo.quality, 0)

        gilded_rose.update_quality()
        self.assertEqual(foo.sell_in, -2)
        self.assertEqual(foo.quality, 0)


    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 1, 2)]
        gilded_rose = GildedRose(items)
        brie = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(brie.sell_in, 0)
        self.assertEqual(brie.quality, 3)

        gilded_rose.update_quality()
        self.assertEqual(brie.sell_in, -1)
        self.assertEqual(brie.quality, 5)

        gilded_rose.update_quality()
        self.assertEqual(brie.sell_in, -2)
        self.assertEqual(brie.quality, 7)


    def test_quality_cannot_exceed_50(self):
        items = [Item("Aged Brie", 2, 49)]
        gilded_rose = GildedRose(items)
        brie = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(brie.sell_in, 1)
        self.assertEqual(brie.quality, 50)

        gilded_rose.update_quality()
        self.assertEqual(brie.sell_in, 0)
        self.assertEqual(brie.quality, 50)

        gilded_rose.update_quality()
        self.assertEqual(brie.sell_in, -1)
        self.assertEqual(brie.quality, 50)


    def test_sulfuras_does_not_decrease_in_quality_and_does_not_need_to_be_sold(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        item = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

    def test_backstage_passes_increase_in_value(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)]
        gilded_rose = GildedRose(items)
        item = gilded_rose.items[0]

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 11)
        self.assertEqual(item.quality, 21)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 22)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 24)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 8)
        self.assertEqual(item.quality, 26)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 32)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 35)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 47)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 0)


    def test_multiple_items(self):
        backstage_pass = Item("Backstage passes to a TAFKAL80ETC concert", 9, 20)
        aged_brie = Item("Aged Brie", 5, 10)
        normal_item = Item("foo", 5, 4)
        items = [backstage_pass, aged_brie, normal_item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        self.assertEqual(backstage_pass.quality, 22)
        self.assertEqual(aged_brie.quality, 11)
        self.assertEqual(normal_item.quality, 3)


    def test_creating_item_with_quality_higher_than_50_throws_error(self):
        # Except for sulfuras
        pass

    def test_catch_default_value_for_sulfuras(self):
        # Or throw error or something when sulfuras does not have the expected value
        pass

if __name__ == '__main__':
    unittest.main()
