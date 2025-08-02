SELECT item_id, item_name, rarity
FROM item_info
WHERE item_id IN (SELECT t.item_id
                 FROM item_tree AS t, item_info AS i
                 WHERE i.rarity = 'RARE' AND t.parent_item_id = i.item_id)
ORDER BY item_id DESC;