import discord
import asyncio
import aiohttp
from datetime import datetime, timezone
from colorama import Fore, Style, init
import random

init(autoreset=True)

COLORS = {
    'cyan': Fore.CYAN,
    'magenta': Fore.MAGENTA,
    'yellow': Fore.YELLOW,
    'green': Fore.GREEN,
    'red': Fore.RED,
    'white': Fore.WHITE,
    'bright': Style.BRIGHT,
    'reset': Style.RESET_ALL
}

EMOJIS = {
    'discord_employee': '<:discordstaff:1462545486044074218>',
    'partnered_server_owner': '<:discordpartner:1462545451403313152>',
    'hypesquad_events': '<:hypesquadevents:1462545625026527355>',
    'bughunter': '<:discordbughunter1:1462545246930866475>',
    'bughuntergold': '<:discordbughunter2:1462544674865807645>',
    'bravery': '<:hypesquadbravery:1462545566935290058>',
    'brilliance': '<:hypesquadbrilliance:1462545593791549460>',
    'balance': '<:hypesquadbalance:1462545536501416040>',
    'early_supporter': '<:discordearlysupporter:1462545300710232216>',
    'early_verified_bot_developer': '<:discordbotdev:1462545206158033027>',
    'moderatorprogramsalumni': '<:discordmod:1462545336131129535>',
    'active_developer': '<:activedev:1147277422337720462>',
    'crown2': '<a:crown2:1413222572090331337>',
    'idcard': '<:idcard:1413222293869432882>',
    'badgespremium': '<:badgespremium:1413230008872210454>',
    'cards': '<:cards:1413230537958625330>',
    'nitro': '<:discordnitro:1462545376946159678>',
    'nitro_bronze': '<:bronze:1462546149079519313>',
    'nitro_silver': '<:silver:1462546147401793722>',
    'nitro_gold': '<:gold:1462546140321939517>',
    'nitro_platinum': '<:platinum:1462546142972874894>',
    'nitro_diamond': '<:diamond:1462546150354845851>',
    'nitro_emerald': '<:emerald:1462546138631639112>',
    'nitro_ruby': '<:ruby:1462546145220755690>',
    'nitro_fire': '<:opal:1462546141731098695>',
    'boost1': '<:discordboost1:1462546187751002205>',
    'boost2': '<:discordboost2:1462546229161623758>',
    'boost3': '<:discordboost3:1462546258030755981>',
    'boost4': '<:discordboost4:1462546284647809290>',
    'boost5': '<:discordboost5:1462546311587827763>',
    'boost6': '<:discordboost6:1462546341304729662>',
    'boost7': '<:discordboost7:1462546372057235778>',
    'boost8': '<:discordboost8:1462546396589592839>',
    'boost9': '<:discordboost9:1462546423450042569>',
}

TARGET_BADGES = {
    1 << 0: {'emoji': EMOJIS['discord_employee'], 'name': 'Discord Employee'},  # rare
    1 << 1: {'emoji': EMOJIS['partnered_server_owner'], 'name': 'Partner'},  # rare
    1 << 2: {'emoji': EMOJIS['hypesquad_events'], 'name': 'HypeSquad Events'},  # rare
    1 << 3: {'emoji': EMOJIS['bughunter'], 'name': 'Bug Hunter'},  # rare
    1 << 9: {'emoji': EMOJIS['early_supporter'], 'name': 'Early Supporter'},  # rare
    1 << 14: {'emoji': EMOJIS['bughuntergold'], 'name': 'Bug Hunter Gold'},  # rare
    1 << 17: {'emoji': EMOJIS['early_verified_bot_developer'], 'name': 'Verified Bot Dev'},  # rare
    1 << 19: {'emoji': EMOJIS['moderatorprogramsalumni'], 'name': 'Certified Mod'},  # rare
}

ALL_FLAG_BADGES = {
    1 << 0: {'emoji': EMOJIS['discord_employee'], 'name': 'Discord Employee'},
    1 << 1: {'emoji': EMOJIS['partnered_server_owner'], 'name': 'Partner'},
    1 << 2: {'emoji': EMOJIS['hypesquad_events'], 'name': 'HypeSquad Events'},
    1 << 3: {'emoji': EMOJIS['bughunter'], 'name': 'Bug Hunter'},
    1 << 6: {'emoji': EMOJIS['bravery'], 'name': 'HypeSquad Bravery'},
    1 << 7: {'emoji': EMOJIS['brilliance'], 'name': 'HypeSquad Brilliance'},
    1 << 8: {'emoji': EMOJIS['balance'], 'name': 'HypeSquad Balance'},
    1 << 9: {'emoji': EMOJIS['early_supporter'], 'name': 'Early Supporter'},
    1 << 14: {'emoji': EMOJIS['bughuntergold'], 'name': 'Bug Hunter Gold'},
    1 << 17: {'emoji': EMOJIS['early_verified_bot_developer'], 'name': 'Verified Bot Dev'},
    1 << 18: {'emoji': EMOJIS['active_developer'], 'name': 'Active Developer'},
    1 << 19: {'emoji': EMOJIS['moderatorprogramsalumni'], 'name': 'Certified Mod'},
}

NITRO_BADGES = {
    'premium_tenure_1_month': {'emoji': EMOJIS['nitro_bronze'], 'name': 'Bronze Nitro'},
    'premium_tenure_3_month': {'emoji': EMOJIS['nitro_silver'], 'name': 'Silver Nitro'},
    'premium_tenure_6_month': {'emoji': EMOJIS['nitro_gold'], 'name': 'Gold Nitro'},
    'premium_tenure_12_month': {'emoji': EMOJIS['nitro_platinum'], 'name': 'Platinum Nitro'},
    'premium_tenure_24_month': {'emoji': EMOJIS['nitro_diamond'], 'name': 'Diamond Nitro'},
    'premium_tenure_36_month': {'emoji': EMOJIS['nitro_emerald'], 'name': 'Emerald Nitro'},
    'premium_tenure_60_month': {'emoji': EMOJIS['nitro_ruby'], 'name': 'Ruby Nitro'},
    'premium_tenure_72_month': {'emoji': EMOJIS['nitro_fire'], 'name': 'Fire Nitro'},
    'premium_tenure_1_month_v2': {'emoji': EMOJIS['nitro_bronze'], 'name': 'Bronze Nitro'},
    'premium_tenure_3_month_v2': {'emoji': EMOJIS['nitro_silver'], 'name': 'Silver Nitro'},
    'premium_tenure_6_month_v2': {'emoji': EMOJIS['nitro_gold'], 'name': 'Gold Nitro'},
    'premium_tenure_12_month_v2': {'emoji': EMOJIS['nitro_platinum'], 'name': 'Platinum Nitro'},
    'premium_tenure_24_month_v2': {'emoji': EMOJIS['nitro_diamond'], 'name': 'Diamond Nitro'},
    'premium_tenure_36_month_v2': {'emoji': EMOJIS['nitro_emerald'], 'name': 'Emerald Nitro'},
    'premium_tenure_60_month_v2': {'emoji': EMOJIS['nitro_ruby'], 'name': 'Ruby Nitro'},
    'premium_tenure_72_month_v2': {'emoji': EMOJIS['nitro_fire'], 'name': 'Fire Nitro'},
}

BOOST_BADGES = {
    'guild_booster_lvl1': {'emoji': EMOJIS['boost1'], 'name': 'Boost Level 1'},
    'guild_booster_lvl2': {'emoji': EMOJIS['boost2'], 'name': 'Boost Level 2'},
    'guild_booster_lvl3': {'emoji': EMOJIS['boost3'], 'name': 'Boost Level 3'},
    'guild_booster_lvl4': {'emoji': EMOJIS['boost4'], 'name': 'Boost Level 4'},
    'guild_booster_lvl5': {'emoji': EMOJIS['boost5'], 'name': 'Boost Level 5'},
    'guild_booster_lvl6': {'emoji': EMOJIS['boost6'], 'name': 'Boost Level 6'},
    'guild_booster_lvl7': {'emoji': EMOJIS['boost7'], 'name': 'Boost Level 7'},
    'guild_booster_lvl8': {'emoji': EMOJIS['boost8'], 'name': 'Boost Level 8'},
    'guild_booster_lvl9': {'emoji': EMOJIS['boost9'], 'name': 'Boost Level 9'},
}

EMBED_COLORS = [0xFF1493, 0x9B59B6, 0x3498DB, 0xE91E63, 0x00CED1, 0xFF6B6B]
FOOTER = {
    'text': 'fantasy',
    'icon_url': 'https://i.hizliresim.com/l3gua78.jpg'
}

def log(msg, color=''):
    print(f"{color}{msg}{COLORS['reset']}")

def has_rare_badge(public_flags):
    for flag_value in TARGET_BADGES.keys():
        if public_flags & flag_value:
            return True
    return False

def get_all_badges_from_flags(public_flags):
    badges = []
    for flag_value, badge_info in ALL_FLAG_BADGES.items():
        if public_flags & flag_value:
            badges.append({
                'emoji': badge_info['emoji'],
                'name': badge_info['name']
            })
    return badges

def add_profile_badges(badges, profile_data):
    if not profile_data:
        return badges
    profile_badges = []
    user_profile = profile_data.get('user_profile', {})
    if user_profile:
        profile_badges = user_profile.get('badges', [])
    if not profile_badges:
        profile_badges = profile_data.get('badges', [])
    if not profile_badges:
        user_data = profile_data.get('user', {})
        if user_data:
            profile_badges = user_data.get('badges', [])
    for badge_data in profile_badges:
        badge_id = badge_data.get('id', 'unknown')
        if badge_id in NITRO_BADGES:
            info = NITRO_BADGES[badge_id]
            if not any(b['name'] == info['name'] for b in badges):
                badges.append({'emoji': info['emoji'], 'name': info['name']})
        elif badge_id in BOOST_BADGES:
            info = BOOST_BADGES[badge_id]
            if not any(b['name'] == info['name'] for b in badges):
                badges.append({'emoji': info['emoji'], 'name': info['name']})
    premium_type = profile_data.get('premium_type') or user_profile.get('premium_type')
    if premium_type and not any('Nitro' in b['name'] for b in badges):
        badges.append({'emoji': EMOJIS['nitro'], 'name': 'Nitro'})
    return badges

async def fetch_profile(session, user_id, token, retries=3):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    url = f'https://discord.com/api/v9/users/{user_id}/profile?with_mutual_guilds=false&with_mutual_friends=false'
    for attempt in range(retries):
        try:
            async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status == 200:
                    return await resp.json()
                elif resp.status == 429:
                    retry_after = float(resp.headers.get('Retry-After', '5'))
                    log(f'  Rate limited, waiting {retry_after}s...', COLORS['yellow'])
                    await asyncio.sleep(retry_after + 1)
                    continue
                else:
                    return None
        except asyncio.TimeoutError:
            if attempt < retries - 1:
                await asyncio.sleep(1)
                continue
            return None
        except Exception:
            if attempt < retries - 1:
                await asyncio.sleep(1)
                continue
            return None
    return None

async def send_webhook(session, url, embed, retries=3):
    for attempt in range(retries):
        try:
            async with session.post(url, json={'embeds': [embed]}, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status in [200, 204]:
                    return True
                elif resp.status == 429:
                    retry_after = float(resp.headers.get('Retry-After', '5'))
                    await asyncio.sleep(retry_after + 1)
                    continue
                else:
                    return False
        except:
            if attempt < retries - 1:
                await asyncio.sleep(1)
                continue
            return False
    return False

def create_embed(user_data):
    desc = f"{EMOJIS['idcard']} **ID:** `{user_data['id']}` | <@{user_data['id']}>"
    badges = user_data.get('badges', [])
    if badges:
        badge_emojis = ' '.join([b['emoji'] for b in badges])
        badge_names = ', '.join([b['name'] for b in badges])
        desc += f"\n{EMOJIS['badgespremium']} **Badges:** {len(badges)}\n"
        desc += f"{badge_emojis}\n`{badge_names}`"
    avatar = user_data.get('avatar')
    if avatar:
        ext = 'gif' if avatar.startswith('a_') else 'png'
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_data['id']}/{avatar}.{ext}?size=256"
    else:
        avatar_url = "https://cdn.discordapp.com/embed/avatars/0.png"
    return {
        'title': f"{EMOJIS['crown2']} {user_data['name']}",
        'description': desc,
        'color': random.choice(EMBED_COLORS),
        'thumbnail': {'url': avatar_url},
        'footer': FOOTER,
        'timestamp': datetime.now(timezone.utc).isoformat()
    }

class BadgeScraper(discord.Client):
    def __init__(self, guild_id, webhook_url, token):
        super().__init__()
        self.target_guild_id = int(guild_id)
        self.webhook_url = webhook_url
        self.token = token
        self.session = None
        self.sent_count = 0

    async def on_ready(self):
        log(f'✓ Logged in as {self.user}\n', COLORS['green'])
        try:
            self.session = aiohttp.ClientSession()
            guild = self.get_guild(self.target_guild_id)
            if not guild:
                try:
                    guild = await self.fetch_guild(self.target_guild_id)
                except:
                    log(f'Guild bulunamadı!', COLORS['red'])
                    await self.cleanup()
                    return
            log(f'Guild: {guild.name}', COLORS['cyan'])
            log(f'Fetching members...', COLORS['cyan'])
            members = await guild.fetch_members()
            members = [m for m in members if not m.bot]
            log(f'✓ {len(members)} members\n', COLORS['green'])
            log('Phase 1: Finding RARE badge users...', COLORS['cyan'])
            log(f'Target badges: {", ".join([b["name"] for b in TARGET_BADGES.values()])}', COLORS['white'])
            target_members = []
            for member in members:
                public_flags = member.public_flags.value if member.public_flags else 0
                if has_rare_badge(public_flags):
                    target_members.append(member)
            log(f'✓ Found {len(target_members)} users with RARE badges\n', COLORS['green'])
            if len(target_members) == 0:
                log('No rare badge users found!', COLORS['yellow'])
                await self.cleanup()
                return
            start_embed = {
                'title': f"{EMOJIS['crown2']} Scan Started",
                'description': f"**Server:** `{guild.name}`\n**Total Members:** `{len(members)}`\n**Rare Badge Users:** `{len(target_members)}`",
                'color': 0xFF1493,
                'footer': FOOTER,
                'timestamp': datetime.now(timezone.utc).isoformat()
            }
            await send_webhook(self.session, self.webhook_url, start_embed)
            log('Phase 2: Fetching ALL badges & sending...', COLORS['cyan'])
            for i, member in enumerate(target_members, 1):
                public_flags = member.public_flags.value if member.public_flags else 0
                badges = get_all_badges_from_flags(public_flags)
                profile = await fetch_profile(self.session, member.id, self.token)
                badges = add_profile_badges(badges, profile)
                self.sent_count += 1
                user_data = {
                    'name': member.display_name,
                    'id': str(member.id),
                    'avatar': member.avatar.key if member.avatar else None,
                    'badges': badges
                }
                embed = create_embed(user_data)
                success = await send_webhook(self.session, self.webhook_url, embed)
                if success:
                    badge_names = ', '.join([b['name'] for b in badges])
                    log(f'✓ [{i}/{len(target_members)}] {member.display_name} ({len(badges)} badges)', COLORS['green'])
                    log(f'   {badge_names}', COLORS['cyan'])
                else:
                    log(f'✗ [{i}/{len(target_members)}] {member.display_name} - webhook failed', COLORS['red'])
                await asyncio.sleep(0.4)
            log(f'✓ Complete! Sent {self.sent_count} users', COLORS['green'])
            final_embed = {
                'title': f"{EMOJIS['crown2']} Scan Complete",
                'description': f"**Total Scanned:** `{len(members)}`\n**Rare Users Sent:** `{self.sent_count}`",
                'color': 0x00FF00,
                'footer': FOOTER,
                'timestamp': datetime.now(timezone.utc).isoformat()
            }
            await send_webhook(self.session, self.webhook_url, final_embed)
        except Exception as e:
            log(f'Error: {e}', COLORS['red'])
            import traceback
            traceback.print_exc()
        finally:
            await self.cleanup()
    async def cleanup(self):
        if self.session:
            await self.session.close()
        await self.close()

async def main():
    print(f"{COLORS['cyan']}Token: {COLORS['reset']}", end='')
    token = input().strip()
    print(f"{COLORS['cyan']}Server ID: {COLORS['reset']}", end='')
    guild_id = input().strip()
    print(f"{COLORS['cyan']}Webhook: {COLORS['reset']}", end='')
    webhook = input().strip()
    log('\nStarting...\n', COLORS['cyan'])
    client = BadgeScraper(guild_id, webhook, token)
    try:
        await client.start(token)
    except discord.LoginFailure:
        log('Invalid token!', COLORS['red'])
    except Exception as e:
        log(f'Error: {e}', COLORS['red'])

if __name__ == '__main__':
    asyncio.run(main())
