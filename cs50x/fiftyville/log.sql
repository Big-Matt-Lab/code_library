-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Used .schema and .table as necessary to seek clues
-- Looked at crime scene reports on the reported day and time
.schema
SELECT id, description FROM crime_scene_reports WHERE
month = 7 AND day = 28 AND year = 2025 AND street = 'Humphrey Street'
-- From the previous query we learned the id of the CSR is 295
-- Reading the description we shift our focus to the bakery look at bakery security logs
--  and read interview transcripts
.schema interviews
SELECT id, name, transcript FROM interviews WHERE
    month = 7 AND year = 2025 AND day = 28;
-- After the query we learned Ruth, Eugene, and Raymond are witnesses
-- Ruth saw a car at the bakery
.schema bakery_security_logs
SELECT id, minute, license_plate, activity FROM bakery_security_logs WHERE
    year = 2025 AND month = 7 AND day = 28 AND hour = 10 AND minute > 15;
-- Witness statements stated the alleged thief left 10 minutes after the crime.
-- There is one log entry at the reported time where a car left the lot. Might be the thief, might be getaway driver
.schema people
SELECT id, name, phone_number, passport_number FROM people WHERE
    license plate = '1106N58';
-- This query returned Taylor, id # 449774, phone (286) 555-6063, and passport 1988161715
.schema passengers
SELECT flight_id FROM passengers WHERE
    passport_number = 1988161715;
-- *** From that query we learned that Taylor did take a flight, id 36. But did he fly alone, where did he go?
-- *** We'll explore Taylor further. Now let's follow up on Eugene's interview.
SELECT id, account_number, transaction_type from atm_transactions WHERE
    year = 2025 AND month = 7 AND day = 28 AND hour >= 9 AND atm_locations = 'Leggett Street';
-- Let's try and find out if Taylor used the atm on the 28th
SELECT name from people
-- With no timestamp the atm info this might not be helpful, let's look at Raymond's statement

