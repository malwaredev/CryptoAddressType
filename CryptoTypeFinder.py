import re

def identify_crypto_address(address):
    # Bitcoin (BTC)
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return f"{address} - BTC (Legacy)"
    if re.match(r'^bc1[ac-hj-np-z02-9]{39,59}$', address):
        return f"{address} - BTC (Segwit)"
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return f"{address} - BTC (P2SH)"

    # Ethereum (ETH) and ERC20 tokens
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return f"{address} - ETH or ERC20"

    # Litecoin (LTC)
    if re.match(r'^[LM3][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return f"{address} - LTC (Legacy)"
    if re.match(r'^ltc1[a-zA-HJ-NP-Z0-9]{25,39}$', address):
        return f"{address} - LTC (Bech32)"
    if re.match(r'^ltcn[a-zA-HJ-NP-Z0-9]{25,34}$', address):
        return f"{address} - LTC (Legacy)"

    # Monero (XMR)
    if re.match(r'^4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$', address):
        return f"{address} - XMR"

    # Stellar (XLM)
    if re.match(r'^G[a-zA-Z0-9]{55}$', address):
        return f"{address} - XLM"

    # Tron (TRX)
    if re.match(r'^T[a-zA-Z0-9]{33}$', address):
        return f"{address} - TRX"

    # Zcash (ZEC)
    if re.match(r'^t1[a-zA-Z0-9]{33}$', address):
        return f"{address} - ZEC (Transparent)"
    if re.match(r'^zs1[a-zA-Z0-9]{75}$', address):
        return f"{address} - ZEC (Shielded)"

    # Dogecoin (DOGE)
    if re.match(r'^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$', address):
        return f"{address} - DOGE"

    # Cardano (ADA)
    if re.match(r'^addr1[a-z0-9]+$', address):
        return f"{address} - ADA"

    # Bitcoin Cash (BCH)
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return f"{address} - BCH (Legacy)"
    if re.match(r'^(bitcoincash:)?(q|p)[a-z0-9]{41}$', address):
        return f"{address} - BCH (CashAddr)"

    # Ripple (XRP)
    if re.match(r'^r[0-9a-zA-Z]{24,34}$', address):
        return f"{address} - XRP"

    # Polkadot (DOT)
    if re.match(r'^1[a-zA-Z0-9]{47}$', address):
        return f"{address} - DOT"

    # Tether (USDT)
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return f"{address} - USDT (ERC20)"
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return f"{address} - USDT (BTC)"
    if re.match(r'^[LM][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return f"{address} - USDT (LTC)"

    # Solana (SOL)
    if re.match(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$', address):
        return f"{address} - SOL"

    # Algorand (ALGO)
    if re.match(r'^[A-Z2-7]{58}$', address):
        return f"{address} - ALGO"

    # Cosmos (ATOM)
    if re.match(r'^cosmos1[a-z0-9]{38}$', address):
        return f"{address} - ATOM"

    # Tezos (XTZ)
    if re.match(r'^tz1[a-zA-Z0-9]{33}$', address):
        return f"{address} - XTZ"

    # EOS
    if re.match(r'^[a-z1-5]{12}$', address):
        return f"{address} - EOS"

    # IOTA
    if re.match(r'^[A-Z9]{90}$', address):
        return f"{address} - IOTA"

    # Nano
    if re.match(r'^(xrb_|nano_)[13][13456789abcdefghijkmnopqrstuwxyz]{59}$', address):
        return f"{address} - NANO"

    # Zilliqa (ZIL)
    if re.match(r'^zil1[a-zA-Z0-9]{38}$', address):
        return f"{address} - ZIL"

    # Decred (DCR)
    if re.match(r'^D[a-zA-Z0-9]{33}$', address):
        return f"{address} - DCR"

    # Dash
    if re.match(r'^X[1-9A-HJ-NP-Za-km-z]{33}$', address):
        return f"{address} - DASH"

    # Filecoin (FIL)
    if re.match(r'^f[0-9]+$', address):
        return f"{address} - FIL"

    # Hedera (HBAR)
    if re.match(r'^0\.0\.[0-9]+$', address):
        return f"{address} - HBAR"

    # VeChain (VET)
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return f"{address} - VET"

    # Avalanche (AVAX)
    if re.match(r'^X-avax1[a-z0-9]{39}$', address):
        return f"{address} - AVAX"

    # Terra (LUNA)
    if re.match(r'^terra1[a-z0-9]{38}$', address):
        return f"{address} - LUNA"

    # Harmony (ONE)
    if re.match(r'^one1[a-z0-9]{38}$', address):
        return f"{address} - ONE"

    # Elrond (EGLD)
    if re.match(r'^erd1[a-zA-Z0-9]{58}$', address):
        return f"{address} - EGLD"

    # Flow
    if re.match(r'^0x[a-fA-F0-9]{16}$', address):
        return f"{address} - FLOW"

    # Fantom (FTM)
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return f"{address} - FTM"

    # Polygon (MATIC)
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return f"{address} - MATIC"

    # Ontology (ONT)
    if re.match(r'^A[A-Za-z0-9]{33}$', address):
        return f"{address} - ONT"

    # ICON (ICX)
    if re.match(r'^hx[a-fA-F0-9]{40}$', address):
        return f"{address} - ICX"

    # Horizen (ZEN)
    if re.match(r'^z[a-zA-Z0-9]{34}$', address):
        return f"{address} - ZEN"

    # Ravencoin (RVN)
    if re.match(r'^R[a-zA-Z0-9]{33}$', address):
        return f"{address} - RVN"

    # Stacks (STX)
    if re.match(r'^[SM][A-Z0-9]{26,35}$', address):
        return f"{address} - STX"

    # Nervos (CKB)
    if re.match(r'^ckb1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{42}$', address):
        return f"{address} - CKB"

    # Secret Network (SCRT)
    if re.match(r'^secret1[a-z0-9]{38}$', address):
        return f"{address} - SCRT"

    # Band Protocol (BAND)
    if re.match(r'^band1[a-z0-9]{38}$', address):
        return f"{address} - BAND"

    # Oasis Network (ROSE)
    if re.match(r'^oasis1[a-z0-9]{58}$', address):
        return f"{address} - ROSE"

    # Binance Coin (BNB)
    if re.match(r'^bnb1[a-z0-9]{38}$', address):
        return f"{address} - BNB"

    return f"{address} - Unknown"

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        results = [identify_crypto_address(line.strip()) for line in f]
        out.write('\n'.join(results))

    print(f"Results saved to {output_file}")
