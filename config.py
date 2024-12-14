import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import threading
import time
import csv
from io import StringIO
import json
import os
import atexit
from telebot import apihelper
from datetime import datetime
from zoneinfo import ZoneInfo
import sqlite3
import logging

header('Content-type:text/plain;charset=utf-8');

// URL-адрес платежной формы
linktoform = 'https://demo.payform.ru/';

// Данные, которые будут отправлены на сервер Продамус
data = [
    'order_id' => '123456', // Уникальный идентификатор заказа
    'customer_phone' => '+79278820060', // Телефон клиента
    'customer_email' => 'site_testing@prodamus.ru', // Email клиента
    'products' => [
        [
            'name' => 'Личный бренд', // Наименование товара
            'price' => 1590.00, // Цена товара
            'quantity' => 1 // Количество товара
        ]
    ],
    'do' => 'link', // Действие для получения ссылки
    'urlReturn' => 'https://demo.payform.ru/demo-return', // URL для возврата
    'urlSuccess' => 'https://demo.payform.ru/demo-success', // URL для успешной оплаты
    'sys' => '', // Код системы, если требуется
    'discount_value' => 100.00, // Сумма скидки
    'link_expired' => '2023-12-31 23:59:59', // Срок действия ссылки
    'payment_method' => 'AC, ACkztjp, SBP, QW' // Доступные методы оплаты
];

// Генерация подписи запроса
require_once __DIR__ . '/Hmac.php';
secret_key = '2y2aw4oknnke80bp1a8fniwuuq7tdkwmmuq7vwi4nzbr8z1182ftbn6p8mhw3bhz';
data['signature'] = Hmac::create(data, secret_key);

// Формирование ссылки на оплату
link = linktoform . '?' . http_build_query(data);

// Вывод ссылки
echo link;