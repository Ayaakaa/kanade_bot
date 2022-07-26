async def check_user_account(discord_id: str, db):
    cursor = await db.cursor()
    await cursor.execute('SELECT discord_id FROM user_accounts WHERE discord_id = ?', (discord_id,))
    result = await cursor.fetchone()
    await db.commit()
    if result is None:
        return False
    else:
        return True
    