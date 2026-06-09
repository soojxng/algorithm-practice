-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', f.board_id, '/', f.file_id, f.file_name, f.file_ext) AS file_path
FROM used_goods_board AS b, used_goods_file AS f
WHERE b.board_id = f.board_id AND b.views = (SELECT MAX(views) FROM used_goods_board)
ORDER BY f.file_id DESC;