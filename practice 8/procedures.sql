-- Procedure 1: insert or update contact
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$;



-- Procedure 2: bulk insert with validation
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names TEXT[],
    phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names,1) LOOP
        
        IF phones[i] ~ '^[0-9]+$' THEN
        
            IF EXISTS (SELECT 1 FROM contacts WHERE name = names[i]) THEN
                UPDATE contacts SET phone = phones[i]
                WHERE name = names[i];
            ELSE
                INSERT INTO contacts(name, phone)
                VALUES(names[i], phones[i]);
            END IF;

        ELSE
            RAISE NOTICE 'Invalid phone number: %', phones[i];
        END IF;

    END LOOP;
END;
$$;



-- Procedure 3: delete by name or phone
CREATE OR REPLACE PROCEDURE delete_contact(identifier TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = identifier
       OR phone = identifier;
END;
$$;
