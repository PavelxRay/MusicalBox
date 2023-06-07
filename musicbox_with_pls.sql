-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Июн 08 2023 г., 01:42
-- Версия сервера: 10.4.28-MariaDB
-- Версия PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `musicbox`
--

-- --------------------------------------------------------

--
-- Структура таблицы `autor`
--

CREATE TABLE `autor` (
  `Autor_id` int(11) NOT NULL,
  `AutorName` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `autor`
--

INSERT INTO `autor` (`Autor_id`, `AutorName`) VALUES
(1, 'Yaosobi'),
(2, 'Кэнси Ёнэдзу'),
(3, 'Натали'),
(4, 'Король и Шут'),
(5, 'Дайте танк (!)'),
(6, 'NUEKI, TOLCHONOV'),
(7, 'HOYO-MiX'),
(8, 'Дискотека Авария'),
(9, 'Алла Пугачева'),
(10, 'Лепс'),
(11, 'Кино'),
(12, 'Powerwolf'),
(13, 'Hanae'),
(14, 'Артур Пирожков'),
(15, 'Yukopi'),
(16, 'Kopatuch feat Karkaruch, Barash'),
(17, 'Lisa'),
(18, 'Shinsei Kamattechan'),
(19, 'Дэвид Сильвиан'),
(20, 'Комбинация'),
(21, 'Валерий Мармеладзе'),
(22, 'Marie Madeleine'),
(23, 'Molchat Doma'),
(24, 'Где Фантом?'),
(25, 'CHERNIKOVSKAYA HATA'),
(26, 'Nightmare'),
(27, 'Yoko Takahashi'),
(28, 'Goose House'),
(29, 'JAM Project'),
(30, 'Masatoshi Ono'),
(31, 'Konomi Suzuki'),
(32, 'Seatbelts'),
(33, 'FUNKIST'),
(34, 'Oral Cigarettes'),
(35, 'Super Eurobeat - Dave Rodgers'),
(36, 'Mob Choir'),
(37, 'Монеточка'),
(38, 'Айдамир Мугу'),
(39, 'Сатисфакция'),
(40, 'ЧайФ');

-- --------------------------------------------------------

--
-- Структура таблицы `genre`
--

CREATE TABLE `genre` (
  `Genre_ID` int(11) NOT NULL,
  `Genre` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `genre`
--

INSERT INTO `genre` (`Genre_ID`, `Genre`) VALUES
(1, 'Рок'),
(2, 'Поп'),
(3, 'Реп'),
(4, 'Phonk'),
(5, 'Лирика');

-- --------------------------------------------------------

--
-- Структура таблицы `language`
--

CREATE TABLE `language` (
  `Language_id` int(4) NOT NULL,
  `Language` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `language`
--

INSERT INTO `language` (`Language_id`, `Language`) VALUES
(1, 'Русский'),
(2, 'Английский'),
(3, 'Японский'),
(4, 'Без вокала');

-- --------------------------------------------------------

--
-- Структура таблицы `music`
--

CREATE TABLE `music` (
  `Music_id` int(4) NOT NULL,
  `MusicName` varchar(30) NOT NULL,
  `Date` varchar(11) NOT NULL,
  `Autor_id` int(4) NOT NULL,
  `Albom` varchar(30) NOT NULL,
  `Nastroy_id` int(4) NOT NULL,
  `Genre_id` int(4) NOT NULL,
  `Language_id` int(4) NOT NULL,
  `href` text NOT NULL,
  `pl` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `music`
--

INSERT INTO `music` (`Music_id`, `MusicName`, `Date`, `Autor_id`, `Albom`, `Nastroy_id`, `Genre_id`, `Language_id`, `href`, `pl`) VALUES
(1, 'IDOL', '12.04.2023', 1, 'Idol', 2, 5, 3, 'https://www.youtube.com/watch?v=ZRtdQ81jPUQ&ab_channel=Ayase%2FYOASOBI', 2),
(2, 'Kick Back', '10.03.2021', 2, 'Kick Back', 2, 2, 3, 'https://www.youtube.com/watch?v=dFlDRhvM4L0&ab_channel=MAPPACHANNEL', 2),
(3, 'Kamisama Onegai', '24.07.2012', 13, 'single', 3, 5, 3, 'https://www.youtube.com/watch?v=CpDpUewAgpE&ab_channel=Hanae-Topic', 2),
(4, 'туДЫМ-сюДЫМ', '07.06.2020', 14, 'single', 2, 2, 1, 'https://www.youtube.com/watch?v=sW4srCj0bvY&ab_channel=AleksandrRevva', 0),
(5, 'StormBack', '15.03.2023', 15, 'single', 2, 2, 3, 'https://www.youtube.com/watch?v=D6DVTLvOupE&ab_channel=Yukopi', 2),
(6, 'Шубиду', '17.05.2013', 16, 'single', 2, 5, 1, 'https://www.youtube.com/watch?v=s3Ima7fTEbQ&ab_channel=TVSmeshariki', 0),
(7, 'TUTUTUTU', '21.02.2023', 6, 'single', 4, 4, 2, 'https://www.youtube.com/watch?v=QlqVAA67chs&ab_channel=PHONKDOMAIN', 0),
(8, 'Северный флот', '22.03.2004', 4, 'Бунт на корабле', 4, 1, 1, 'https://www.youtube.com/watch?v=RvaSPyvdgkg&ab_channel=V.K.', 0),
(9, 'Танец злобного гения', '11.10.2010', 4, 'Театр демона', 2, 1, 1, 'https://www.youtube.com/watch?v=1LJ_g2bPQDA&ab_channel=%D0%9A%D0%BB%D0%B5%D0%BF%D1%81%D0%B8%D0%B4%D1%80%D0%B0%D0%98%D1%85%D1%82%D0%B8%D1%81', 0),
(10, 'Ели мясо мужики', '16.06.1998', 4, 'Ели мясо мужики', 2, 1, 1, 'https://www.youtube.com/watch?v=vjwOZUrUs6U&ab_channel=MrJawbreaker', 0),
(11, 'Бездельник №1', '05.07.1982', 11, '45', 3, 1, 1, 'https://www.youtube.com/watch?v=imItXBR3-Jg&ab_channel=Kino-Topic', 0),
(12, 'Кукушка', '13.02.1991', 11, 'Черный альбом', 1, 1, 1, 'https://www.youtube.com/watch?v=iXk8QXhr7Fk&ab_channel=Kino-Topic', 0),
(13, 'Хочу перемен', '14.11.1989', 11, 'Последний герой', 1, 1, 1, 'https://www.youtube.com/watch?v=-vdfEZwPd3M&ab_channel=Kino-Topic', 0),
(14, 'Последний герой', '14.11.1989', 11, 'Последний герой', 1, 1, 1, 'https://www.youtube.com/watch?v=ufNgB0POzzY&ab_channel=Kino-Topic', 0),
(15, 'Мама-анархия', '13.05.1986', 11, 'Ночь', 2, 1, 1, 'https://www.youtube.com/watch?v=iREp3xLmAWY&ab_channel=Kino-Topic', 0),
(16, 'My War', '22.03.2021', 18, 'single', 4, 5, 3, 'https://www.youtube.com/watch?v=VK8PKIiAbrM&ab_channel=Yuiiski', 2),
(17, 'For the love of life', '03.07.2004', 19, 'single', 3, 5, 4, 'https://www.youtube.com/watch?v=n86hgIXc1BM&ab_channel=Cthulhu2027', 0),
(18, 'American Boy', '05.12.1990', 20, 'Московская прописка', 2, 2, 1, 'https://www.youtube.com/watch?v=W7hAo28NCXc&ab_channel=%D0%9C%D0%95%D0%94%D0%98%D0%90%D0%A2%D0%95%D0%9A%D0%90%D0%94%D0%96%D0%95%D0%9C', 0),
(19, 'Самый лучший день', '25.02.2011', 10, 'Пенсне', 2, 2, 1, 'https://www.youtube.com/watch?v=kG2jG0eVMhs&ab_channel=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%9A%D1%80%D0%B0%D0%B9%D0%BD%D0%BE%D0%B2', 0),
(20, 'Иностранец', '01.10.2008', 21, 'Вопреки', 1, 2, 1, 'https://www.youtube.com/watch?v=1v0nzSPDjkc&ab_channel=ELLO', 0),
(21, 'Wildfire', '02.05.2023', 7, 'Of Snow and Ember', 4, 5, 3, 'https://www.youtube.com/watch?v=6HQes3jQaDA&ab_channel=HOYO-MiX-Topic', 2),
(22, 'Polumnia Omnia', '18.04.2023', 7, 'The Unfathomable Sand Dunes', 4, 5, 3, 'https://www.youtube.com/watch?v=NLEqRNhv6gs&ab_channel=HOYO-MiX-Topic', 2),
(23, 'Малинки', '17.12.1996', 8, 'single', 2, 2, 1, 'https://www.youtube.com/watch?v=OHFoSazvV88&ab_channel=AidaKazilionien%C4%97', 0),
(24, 'Вы', '26.11.2018', 5, 'На вырост', 1, 5, 1, 'https://www.youtube.com/watch?v=1AgKyDy4d0o&ab_channel=%D0%94%D0%B0%D0%B9%D1%82%D0%B5%D1%82%D0%B0%D0%BD%D0%BA%28%21%29', 1),
(25, 'Альтернатива', '01.10.2020', 5, 'Человеко-часы', 1, 5, 1, 'https://www.youtube.com/watch?v=e7bMKBiRmJw&ab_channel=Daytetank%28%21%29-Topic', 0),
(26, 'Крепость', '01.10.2020', 5, 'Человеко-часы', 3, 5, 1, 'https://www.youtube.com/watch?v=YnSmAfWrXlA&ab_channel=%D0%94%D0%B0%D0%B9%D1%82%D0%B5%D1%82%D0%B0%D0%BD%D0%BA%28%21%29', 1),
(27, 'Люди', '14.11.2020', 5, 'single', 1, 5, 1, 'https://www.youtube.com/watch?v=cbaS7OAT_gA&ab_channel=%D0%94%D0%B0%D0%B9%D1%82%D0%B5%D1%82%D0%B0%D0%BD%D0%BA%28%21%29', 1),
(28, 'Этот мир', '04.11.1977', 9, 'single', 3, 5, 1, 'https://www.youtube.com/watch?v=SVGwTLRgWkg&ab_channel=EkaterinaTsareva', 0),
(29, 'Арлекино', '23.02.1975', 9, 'single', 2, 5, 1, 'https://www.youtube.com/watch?v=tMqbiofmebk&ab_channel=%D0%9C%D1%83%D0%B7%D1%8B%D0%BA%D0%B0%D0%BD%D0%B0%D1%81%D0%BE%D0%B2%D0%B5%D1%82%D1%81%D0%BA%D0%BE%D0%BC%D1%82%D0%B5%D0%BB%D0%B5%D0%B2%D0%B8%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8', 0),
(30, 'Опять метель', '15.04.2008', 9, 'single', 3, 5, 1, 'https://www.youtube.com/watch?v=6ErF1ZjViDY&ab_channel=andreikin', 0),
(31, 'Swimming pool', '31.07.2012', 22, 'good kid', 3, 2, 2, 'https://www.youtube.com/watch?v=eIbTVCXSl5A&ab_channel=MarieMadeleine-Topic', 0),
(32, 'Судно', '07.09.2018', 23, 'Этажи', 3, 2, 1, 'https://www.youtube.com/watch?v=HR5zpFs7YpY&ab_channel=TV-8-301', 1),
(33, 'Клетка', '21.05.2020', 23, 'Этажи', 3, 2, 1, 'https://www.youtube.com/watch?v=c69eHlQrKaY&ab_channel=MolchatDoma', 1),
(34, 'Я тебя люблю', '26.08.2020', 24, 'single', 3, 5, 1, 'https://www.youtube.com/watch?v=Hge8FgcyCKE&ab_channel=%D0%93%D0%B4%D0%B5%D0%A4%D0%B0%D0%BD%D1%82%D0%BE%D0%BC%3F-Topic', 0),
(35, 'Белая Ночь', '30.10.2016', 25, 'single', 3, 5, 1, 'https://www.youtube.com/watch?v=udEdjsfK1Mw&ab_channel=ChernikovskayaHata-Topic', 1),
(36, 'Ты не верь слезам', '30.04.2016', 25, 'single', 3, 5, 1, 'https://www.youtube.com/watch?v=1M_k7b1cAxM&ab_channel=ChernikovskayaHata-Topic', 1),
(37, 'Nochnoe Randevu', '31.05.2016', 25, 'single', 3, 5, 1, 'https://www.youtube.com/watch?v=h9YO1YI0i48&ab_channel=ChernikovskayaHata-Topic', 0),
(38, 'The world', '18.10.2016', 26, 'single', 4, 2, 3, 'https://www.youtube.com/watch?v=kqpO8g3zDQY&ab_channel=Lawier35', 2),
(39, 'A Cruel Angel’s Thesis', '03.10.1996', 27, 'single', 2, 5, 3, 'https://www.youtube.com/watch?v=fShlVhCfHig&ab_channel=AnimeGuy', 2),
(40, 'Hikaru Nara', '19.11.2014', 28, 'single', 1, 5, 3, 'https://www.youtube.com/watch?v=H8MyvOcTy6k&ab_channel=AnimeOST', 2),
(41, 'The Hero!! Set Fire to the Fur', '01.10.2015', 29, 'single', 4, 5, 3, 'https://www.youtube.com/watch?v=TNULwkXLoHE&ab_channel=TurtleTV', 2),
(42, 'Departure!', '03.04.2004', 30, 'single', 2, 5, 3, 'https://www.youtube.com/watch?v=faqmNf_fZlE&ab_channel=CrunchyrollCollection', 2),
(43, 'This Game', '15.07.2017', 31, 'single', 2, 2, 3, 'https://www.youtube.com/watch?v=6CBp4qylX6I&ab_channel=CrunchyrollCollection', 2),
(44, 'Tank!', '03.04.1998', 32, 'Tank! the! Best!', 2, 2, 4, 'https://www.youtube.com/watch?v=n2rVnRwW0h8&ab_channel=videmaxni5', 2),
(45, 'Kyōran Hey Kids!!', '07.10.2015', 34, 'single', 2, 2, 3, 'https://www.youtube.com/watch?v=3oFTHxkOzjE&ab_channel=CrunchyrollDubs\r\n', 2),
(46, 'Deja Vu', '19.04.1998', 35, 'single', 2, 2, 3, 'https://www.youtube.com/watch?v=dv13gl0a-FA&ab_channel=Prettyok', 2),
(47, '99', '29.012019', 36, 'single', 2, 1, 3, 'https://www.youtube.com/watch?v=Bw-5Lka7gPE&ab_channel=CrunchyrollCollection', 2),
(48, 'Папина любовница', '24.12.2020', 37, 'Декоративно-прикладное искусст', 3, 5, 1, 'https://www.youtube.com/watch?v=KKNGlQ5KsaQ&ab_channel=%D0%9C%D0%BE%D0%BD%D0%B5%D1%82%D0%BE%D1%87%D0%BA%D0%B0', 0),
(49, 'Черные глаза', '08.10.2016', 38, 'single', 2, 2, 1, 'https://www.youtube.com/watch?v=XPNNWHU6Io4&ab_channel=Planetmusik', 0),
(50, 'Часы', '10.01.2018', 39, 'На одном дыхании', 3, 1, 1, 'https://www.youtube.com/watch?v=QVi60tapbs8&ab_channel=SergeyK', 1),
(51, 'Товарищ майор', '04.12.2012', 39, 'Ворота. Акустика', 3, 1, 1, 'https://www.youtube.com/watch?v=lczbyJ8gtHE&ab_channel=SergeyK', 1),
(52, 'Девочки свободных взглядов', '11.03.2016', 39, 'Неизданное', 3, 1, 1, 'https://www.youtube.com/watch?v=L0Nq4vI-jeo&ab_channel=ELLO', 0),
(53, 'Чей чай горячей', '25.10.2017', 40, 'Теория струн', 3, 2, 1, 'https://www.youtube.com/watch?v=6VcfrfHE5Z8&ab_channel=%D0%A7%D0%90%D0%99%D0%A4', 1),
(54, 'В её глазах', '22.06.1999', 40, 'Шекогали', 1, 5, 1, 'https://www.youtube.com/watch?v=4mytVOXUWGI&ab_channel=AleuLibra', 1),
(55, 'Army of the Night', '05.05.2015', 12, 'Blessed & Possessed', 4, 1, 2, 'https://www.youtube.com/watch?v=1zN7J64IeBo&ab_channel=NapalmRecords', 0),
(56, 'Demons Are a Girl\'s Best Frien', '10.11.2018', 12, 'The Sacrament of Sin ‍', 4, 1, 2, 'https://www.youtube.com/watch?v=jhK2ev_O-pc&ab_channel=NapalmRecords', 0),
(57, 'We Drink Your Blood', '17.05.2011', 12, 'Blood of the Saints', 4, 1, 2, 'https://www.youtube.com/watch?v=GpxFUo7oxWM&ab_channel=MetalBladeRecords', 0),
(58, 'Venom of Venus', '10.11.2018', 12, 'The Sacrament of Sin ‍', 4, 3, 2, 'https://www.youtube.com/watch?v=dLbcipFIQAU&ab_channel=PowerwolfOfficial', 0),
(59, 'Sanctified with Dynamite', '17.05.2011', 12, 'Blood of the Saints', 4, 1, 2, 'https://www.youtube.com/watch?v=PhiSgXz_l20&ab_channel=MetalBladeRecords', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `nastroy`
--

CREATE TABLE `nastroy` (
  `Nastroy_id` int(11) NOT NULL,
  `NastroyName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `nastroy`
--

INSERT INTO `nastroy` (`Nastroy_id`, `NastroyName`) VALUES
(1, 'Грустно'),
(2, 'Весело'),
(3, 'Покой'),
(4, 'Гнев');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `User_id` int(4) NOT NULL,
  `Login` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `e-mail` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Surname` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`User_id`, `Login`, `Password`, `e-mail`, `Name`, `Surname`) VALUES
(1, 'ShiNOOBu', 'Nastorozhe13', 'hidukoff-pavel@yandex.ru', 'Павел', 'Хайдуков'),
(2, 'Billy', 'AbobA228', 't_anton08@mail.ru', 'Антон', 'Тощев'),
(3, 'PivishkoTyan', 'qwerty123', 'pivishko@mail.ru', 'Анна', 'Ерёмина'),
(5, '1', '1', '1', '1', '1');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`Autor_id`);

--
-- Индексы таблицы `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`Genre_ID`);

--
-- Индексы таблицы `language`
--
ALTER TABLE `language`
  ADD PRIMARY KEY (`Language_id`);

--
-- Индексы таблицы `music`
--
ALTER TABLE `music`
  ADD PRIMARY KEY (`Music_id`),
  ADD KEY `Autor_id` (`Autor_id`),
  ADD KEY `Nastroy_id` (`Nastroy_id`),
  ADD KEY `Genre_id` (`Genre_id`),
  ADD KEY `Language_id` (`Language_id`);

--
-- Индексы таблицы `nastroy`
--
ALTER TABLE `nastroy`
  ADD PRIMARY KEY (`Nastroy_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`User_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `autor`
--
ALTER TABLE `autor`
  MODIFY `Autor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT для таблицы `genre`
--
ALTER TABLE `genre`
  MODIFY `Genre_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `language`
--
ALTER TABLE `language`
  MODIFY `Language_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `music`
--
ALTER TABLE `music`
  MODIFY `Music_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT для таблицы `nastroy`
--
ALTER TABLE `nastroy`
  MODIFY `Nastroy_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `User_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `music`
--
ALTER TABLE `music`
  ADD CONSTRAINT `music_ibfk_1` FOREIGN KEY (`Autor_id`) REFERENCES `autor` (`Autor_id`),
  ADD CONSTRAINT `music_ibfk_2` FOREIGN KEY (`Nastroy_id`) REFERENCES `nastroy` (`Nastroy_id`),
  ADD CONSTRAINT `music_ibfk_3` FOREIGN KEY (`Genre_id`) REFERENCES `genre` (`Genre_ID`),
  ADD CONSTRAINT `music_ibfk_4` FOREIGN KEY (`Language_id`) REFERENCES `language` (`Language_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
