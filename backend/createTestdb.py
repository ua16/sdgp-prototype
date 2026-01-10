from dataclasses import dataclass
import sqlite3

from datetime import datetime, timezone

import utils.faker as faker
from random import choice, randint

from utils.faker.date import soon

db_path = "db_01.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Sqlite doesn't support dates
# so we are storing times as UNIX epoch times as integers, UTC+0

cursor.execute("""
CREATE TABLE IF NOT EXISTS organization (
    organizationID INTEGER PRIMARY KEY AUTOINCREMENT,
    companyName TEXT NOT NULL,
    companyAddress TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    createdAt TEXT NOT NULL,
    orgType TEXT NOT NULL,
    bio TEXT NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    organizationID INTEGER NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    passwordHash TEXT NOT NULL,
    createdAt INTEGER NOT NULL,
    FOREIGN KEY (organizationID) REFERENCES Organization(organizationID)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Quotes (
    quoteID INTEGER PRIMARY KEY AUTOINCREMENT,
    issuingOrgID INTEGER NOT NULL ,
    targetOrgID INTEGER NOT NULL ,
    fee REAL NOT NULL,
    requestID INTEGER NOT NULL,
    FOREIGN KEY (issuingOrgID) REFERENCES Organization(organizationID),
    FOREIGN KEY (targetOrgID) REFERENCES Organization(organizationID),
    FOREIGN KEY (requestID) REFERENCES rfq(rfqID)
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS rfq (
    rfqid INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    cargoType TEXT NOT NULL,
    commodity TEXT,
    hsCode TEXT,
    netWeight REAL,
    height REAL,
    width REAL,
    cargoValue INTEGER NOT NULL,
    deliveryDate INTEGER NOT NULL,
    creationDate INTEGER NOT NULL,
    expiryDate INTEGER NOT NULL,
    needCargoInsurance INTEGER NOT NULL CHECK (needCargoInsurance IN (0, 1)),
    specialInstructions TEXT,
    issuingOrgID INTEGER NOT NULL,
    targetOrgID INTEGER NOT NULL,
    FOREIGN KEY (issuingOrgID) REFERENCES Organization(organizationID),
    FOREIGN KEY (targetOrgID) REFERENCES Organization(organizationID)
);
""")

connection.commit()

# Create the fake data

# Create fake companies
cursor.execute("SELECT organizationID FROM organization;")
results = cursor.fetchall()

if len(results) < 10:
    print("Creating Organizations")
    for i in range(1, 30):
        company = faker.company.Company()
        cursor.execute(
            """
        INSERT INTO Organization (
            companyName,
            companyAddress,
            email,
            phone,
            createdAt,
            orgType,
            bio
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                company.name,
                company.address,
                company.email,
                company.phone,
                int(
                    faker.date.past().replace(tzinfo=timezone.utc).timestamp()
                ),  # Convert to UTC then convert to UNIX float time
                "Carrier",
                "Bio Not Available",
            ),
        )
    connection.commit()


cursor.execute("SELECT organizationID FROM organization;")
companies = cursor.fetchall()

# Create fake RFQs for company with id 1

cursor.execute("SELECT * FROM rfq;")
results = cursor.fetchall()

if len(results) < 50:
    print("Creating RFQs")
    for i in range(1, 70):
        company = choice(companies)
        cursor.execute(
            """
                INSERT INTO rfq (
                    origin,
                    destination,
                    cargoType,
                    commodity,
                    hsCode,
                    netWeight,
                    height,
                    width,
                    cargoValue,
                    deliveryDate,
                    creationDate,
                    expiryDate,
                    needCargoInsurance,
                    specialInstructions,
                    issuingOrgID,
                    targetOrgID
                    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
            (
                faker.airline.iatacode(),  # origin
                faker.airline.iatacode(),  # destination
                choice(["LCL", "FCL"]),  # cargoType
                choice(
                    ["Electronics", "Sporting Goods", "Perishables", "Raw Material"]
                ),  # commodity
                choice(
                    ["8518.30", "9506.99.1500", "1905.90.9030", "7206.10.0000"]
                ),  # hsCode
                randint(1, 200) * 0.75,  # netWeight
                randint(10, 100) * 0.75,  # height
                randint(20, 100) * 0.75,  # width
                randint(5, 400) * 1000,  # cargoValue
                faker.date.future(), # deliveryDate
                faker.date.recent(),  # creationDate
                faker.date.soon(),  # expiryDate
                choice([0, 1]),  # needCargoInsurance
                choice(
                    [
                        "Moisture proofing",
                        "Cushioning required",
                        "Urgent",
                        "NA",
                        "Extra Legal Forms required",
                    ]
                ),  # specialInstructions
                choice(companies)[0],  # issuingOrgID
                1,  # targetOrgID
            ),
        )


connection.commit()


connection.close()
