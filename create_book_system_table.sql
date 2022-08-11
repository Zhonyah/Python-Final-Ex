CREATE TABLE `book_table` (
  `BOOKID` varchar(25) NOT NULL,
  `TITLE` varchar(200) NOT NULL,
  `AUTHOR` varchar(200) NOT NULL,
  `HEADING` varchar(200) NOT NULL,
  `DETAILS` varchar(200) NOT NULL,
  `CATEGORY` varchar(200) NOT NULL,
  `PUBLISHER` varchar(200) NOT NULL,
  `BOOK_TYPE` varchar(200) NOT NULL,
   PRIMARY KEY (`BOOKID`)
);

INSERT INTO `book_table` (`BOOKID`, `TITLE`, `AUTHOR`, `HEADING`, `DETAILS`, `CATEGORY`, `PUBLISHER`, `BOOK_TYPE`) VALUES
('02008635', 'ความลับที่ผู้นำต้องรู้', 'ทองพันชั่ง พงษ์วารินทร์', '-', 'ผู้นำที่ดีต้องมีคุณลักษณะที่พร้อม', 'จิตวิทยา', 'สำนักพิมพ์ธรรมนิติ', 'หนังสือลิขสิทธิ์สำนักพิมพ์'),
('02005520', 'Illustrator CC', 'วสันต์ พึ่งพูลผล', '-', 'หนังสือเล่มนี้ตั้งใจอธิบายความสามารถของโปรแกรมทั้งหมด', 'คอมพิวเตอร์', 'สำนักพิมพ์ IDC Premier', 'หนังสือลิขสิทธิ์สำนักพิมพ์'),
('01000091', 'ผลกระทบจากการทำลายชั้นโอโซน', '	นางเยาวณี บุญวรรณโน', '-', 'ผลกระทบจากการทำลายชั้นโอโซน', 'วิทยาศาสตร์', 'กระทรวงศึกษาธิการ', 'หนังสือเผยแพร่');