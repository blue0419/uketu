import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("アオアシラ"):
        if client.user != message.author:
            # メッセージを書きます
            m =  message.author.name + "さん！アオアシラは火、状態異常はなんでも効きます！弱点は上半身です！クエストお気をつけて！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("紅兜"): 
            # メッセージを書きます
            m =  message.author.name + "さん！紅兜は火、状態異常はなんでも効きます！弱点は頭、上半身です！クエストお気を付けて！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("アカムトルム"):
        m =  message.author.name + "さん！アカムトルムは龍が効きます！弱点は頭です！火、龍やられ、防御力ダウンになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("アグナコトル"):
        m =  message.author.name + "さん！アグナコトルは水が効きます！弱点は溶岩がない時は背中、溶岩がある時は頭と胸です！火やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("アトラルカ"):
        m =  message.author.name + "さん！アトラル・カは雷が効きます！弱点は頭と尻尾です！糸だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("アマツマガツチ"):
        m =  message.author.name + "さん！アマツマガツチは火、龍が効きます！弱点は頭です！水やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("アルセルタス"):
        m = message.author.name + "さん！アルセルタスは雷、毒、爆破が効きます！弱点はお腹です！防御力ダウンになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("アルバトリオン"):
        m =  message.author.name + "さん！アルバトリオンは赤黒時は氷、青白時は龍が効きます！弱点は頭です！火、龍、雷、氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("イビルジョー"):
        m = message.author.name + "さん！イビルジョーは龍、毒が効きます！弱点は頭です！龍やられ、防御力ダウンになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("飢餓イビルジョー"):
        m = message.author.name + "さん！飢餓イビルジョーは雷、毒が効きます！弱点は胸です！龍やられ、防御力ダウンになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("イャンガルルガ"):
        m = message.author.name + "さん！イャンガルルガは水、爆破が効きます！弱点は頭です！火やられ、毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("隻眼"):
        m = message.author.name + "さん！隻眼は水、爆破が効きます！弱点は頭です！火やられ、毒、猛毒、劇毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("イャンクック"):
        m = message.author.name + "さん！イャンクックは氷、毒、麻痺、睡眠が効きます！弱点は頭、翼です！火やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ヴォルガノス"):
        m = message.author.name + "さん！ヴォルガノスは水が効きます！弱点は頭、ひれです！火やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ウカムルバス"):
        m = message.author.name + "さん！ウカムルバスは火が効きます！弱点は頭です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ウラガンキン"):
        m = message.author.name + "さん！ウラガンキンは通常時は水、顎破壊後は龍が効きます！弱点は通常時はお腹、顎破壊後は頭、お腹です！火やられ、睡眠になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("宝纏"):
        m = message.author.name + "さん！宝纏は水が効きます！弱点は通常時は前足、顎破壊後は頭、前足です！火やられ、睡眠になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ウルクスス"):
        m = message.author.name + "さん！ウルクススは火、麻痺が効きます！弱点は頭です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("大雪主"):
        m = message.author.name + "さん！大雪主は火、麻痺が効きます！弱点は頭です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("オオナズチ"):
        m = message.author.name + "さん！オオナズチは火、麻痺が効きます！弱点は頭、翼です！盗み、毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("オストガロア"):
        m = message.author.name + "さん！オストガロアは龍が効きます！弱点は通常時は背中の弱点、頭、粘膜纏い時は背中の弱点、触腕の先端です！火、雷、龍やられ、爆破、麻痺、粘液まみれ、骨まみれになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ガノトトス"):
        m = message.author.name + "さん！ガノトトスは雷、毒、麻痺、睡眠が効きます！弱点は胴、尻尾です！水やられ、睡眠になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ガムート"):
        m = message.author.name + "さん！ガムートは火が効きます！弱点は鼻、頭です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("銀嶺"):
        m = message.author.name + "さん！銀嶺は通常時は火、雷、雪纏い時は火が効きます！弱点は鼻、頭、尻尾です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ガララアジャラ"):
        m = message.author.name + "さん！ガララアジャラは氷が効きます！弱点は頭、後足です！麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("キリン"):
        m = message.author.name + "さん！キリンは火、水が効きます！弱点は頭です！雷やられ、麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("クシャルダオラ"):
        m = message.author.name + "さん！クシャルダオラは龍が効きます！弱点は頭、尻尾です！氷、龍やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("グラビモス"):
        m = message.author.name + "さん！グラビモスは水が効きます！弱点はお腹です！火やられ、睡眠になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ケチャワチャ"):
        m = message.author.name + "さん！ケチャワチャは火が効きます！弱点は頭、尻尾です！水やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ゲネルセルタス"):
        m = message.author.name + "さん！ゲネルセルタスは火、爆破が効きます！弱点は頭です！水やられ、悪臭になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ゲリョス"):
        m = message.author.name + "さん！ゲリョスは火が効きます！弱点は頭、尻尾です！盗み、毒、気絶になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ゴアマガラ"):
        m = message.author.name + "さん！ゴアマガラは火が効きます！弱点は頭、首、後足です！狂龍になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("混沌ゴアマガラ"):
        m = message.author.name + "さん！混沌ゴアマガラは火が効きます！弱点は頭、後足です！狂龍になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ザボアザギル"):
        m = message.author.name + "さん！ザボアザギルは雷が効きます！弱点はお腹です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("シャガルマガラ"):
        m = message.author.name + "さん！シャガルマガラは龍が効きます！弱点は頭です！狂龍になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ショウグンギザミ"):
        m = message.author.name + "さん！ショウグンギザミは雷が効きます！弱点は通常時は頭、ヤド破壊後は頭、ヤド内です！水やられ、裂傷になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("鎧裂"):
        m = message.author.name + "さん！鎧裂は雷が効きます！弱点は通常時は頭、後足、ヤド破壊後は頭、ヤド内です！水やられ、裂傷、防御力ダウンになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ジンオウガ"):
        m = message.author.name + "さん！ジンオウガは氷が効きます！弱点は通常時は頭、超帯電時は頭、背中です！雷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("金雷公"):
        m = message.author.name + "さん！金雷公は氷が効きます！弱点は頭、背中です！雷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("セルレギオス"):
        m = message.author.name + "さん！セルレギオスは雷が効きます！弱点はお腹、首です！裂傷になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ダイミョウザザミ"):
        m = message.author.name + "さん！ダイミョウザザミは火、雷が効きます！弱点は頭です！水やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("矛砕"):
        m = message.author.name + "さん！矛砕は雷が効きます！弱点は頭です！水やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("タマミツネ"):
        m = message.author.name + "さん！タマミツネは雷が効きます！弱点は頭、背中です！水やられ、泡まみれになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("天眼"):
        m = message.author.name + "さん！天眼は通常時は龍、怒り時は雷が効きます！弱点は背ビレです！水、火やられ、泡まみれになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ディノバルド"):
        m = message.author.name + "さん！ディノバルドは水、毒が効きます！弱点は通常時は頭、赤熱時は尻尾です！火やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("燼滅刃"):
        m = message.author.name + "さん！燼滅刃は水、毒が効きます！弱点は背中、喉です！火やられ、爆破になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("テオテスカトル"):
        m = message.author.name + "さん！テオテスカトルは通常時は水、怒り時は龍が効きます！弱点は尻尾です！火やられ、爆破になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ディアブロス"):
        m = message.author.name + "さん！ディアブロスは氷、毒が効きます！弱点は尻尾、翼膜です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("鏖魔"):
        m = message.author.name + "さん！鏖魔は水、毒が効きます！弱点は尻尾、翼膜です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ティガレックス"):
        m = message.author.name + "さん！ティガレックスは雷が効きます！弱点は頭です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("荒鉤爪"):
        m = message.author.name + "さん！荒鉤爪は雷が効きます！弱点は頭です！氷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("テツカブラ"):
        m = message.author.name + "さん！テツカブラは水、毒、爆破が効きます！弱点は通常時は頭、尻尾膨張時は尻尾です！氷やられ、滅気になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("岩穿"):
        m = message.author.name + "さん！岩穿は水、毒、爆破が効きます！弱点は頭です！氷やられ、滅気、気絶になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスイーオス"):
        m = message.author.name + "さん！ドスイーオスは水、雷、麻痺、睡眠、爆破が効きます！弱点は体です！毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスガレオス"):
        m = message.author.name + "さん！ドスガレオスは氷、毒、睡眠が効きます！弱点は首、背中です！水やられ、麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスギアノス"):
        m = message.author.name + "さん！ドスギアノスは火、毒、麻痺、睡眠が効きます！弱点は頭です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスゲネポス"):
        m = message.author.name + "さん！ドスゲネポスは氷、毒、睡眠、爆破が効きます！弱点は頭です！麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスファンゴ"):
        m = message.author.name + "さん！ドスファンゴは雷、毒、睡眠が効きます！弱点は頭です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスマッカオ"):
        m = message.author.name + "さん！ドスマッカオは火、毒、爆破が効きます！弱点は頭、尻尾です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドスランポス"):
        m = message.author.name + "さん！ドスランポスは氷、毒、麻痺、睡眠が効きます！弱点は頭です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドドブランゴ"):
        m = message.author.name + "さん！ドドブランゴは火が効きます！弱点は頭です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ドボルベルク"):
        m = message.author.name + "さん！ドボルベルクは火、毒、睡眠が効きます！弱点は通常時は頭、コブ破壊後はコブです！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ナルガクルガ"):
        m = message.author.name + "さん！ナルガクルガは雷が効きます！弱点は頭です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("白疾風"):
        m = message.author.name + "さん！白疾風は雷が効きます！弱点は頭です！裂傷になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ネルスキュラ"):
        m = message.author.name + "さん！ネルスキュラは麻痺、爆破が効いて通常時は火、皮破壊後は雷が効きます！弱点は通常時はトゲ、頭、皮破壊後は頭、お腹です！毒、猛毒、睡眠、糸拘束になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("バサルモス"):
        m = message.author.name + "さん！バサルモスは龍、睡眠が効きます！弱点は通常時はお腹、足、お腹破壊後は、お腹です！火やられ、毒、猛毒、睡眠になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ババコンガ"):
        m = message.author.name + "さん！ババコンガは火が効きます！弱点は頭です！火やられ、毒、麻痺、悪臭になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ハプルボッカ"):
        m = message.author.name + "さん！ハプルボッカは氷が効きます！弱点は口内、エラ、鼻です！水やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("バルファルク"):
        m = message.author.name + "さん！バルファルクは火、水、雷、氷が効きます！弱点は翼脚です！龍やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ブラキディオス"):
        m = message.author.name + "さん！ブラキディオスは水が効きます！弱点は頭、尻尾です！爆破になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("臨界ブラキディオス"):
        m = message.author.name + "さん！臨界ブラキディオスは氷が効きます！弱点は頭、尻尾です！爆破になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("フルフル"):
        m = message.author.name + "さん！フルフルは火、毒が効きます！弱点は頭、首です！雷やられ、麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ベリオロス"):
        m = message.author.name + "さん！ベリオロスは火が効きます！弱点は頭、お腹です！氷やられ、雪だるまになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ボルボロス"):
        m = message.author.name + "さん！ボルボロスは爆破が効いて通常時は火、泥纏い時は水が効きます！弱点は前足、尻尾です！泥まみれになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ホロロホルル"):
        m = message.author.name + "さん！ホロロホルルは水が効きます！弱点は頭です！睡眠、混乱になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("朧隠"):
        m = message.author.name + "さん！朧隠は水が効きます！弱点は頭です！睡眠、混乱、盗みになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ミラボレアス"):
        m = message.author.name + "さん！ミラボレアスは龍が効きます！弱点は頭です！火、龍やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ミラバルカン"):
        m = message.author.name + "さん！ミラバルカンは龍、怒り時には氷も効きます！弱点は通常時は頭、怒り時は頭、首です！火やられ、爆破になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ミラルーツ"):
        m = message.author.name + "さん！ミラルーツは龍が効き、怒り時には何も効きません！弱点は通常時は頭、怒り時には頭、首です！雷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ラージャン"):
        m = message.author.name + "さん！ラージャンは氷が効きます！弱点は頭です！雷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("激昂ラージャン"):
        m = message.author.name + "さん！激昂ラージャンは氷が効きます！弱点は頭です！雷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ライゼクス"):
        m = message.author.name + "さん！ライゼクスは氷が効きます！弱点は通常時は頭、電荷時は頭、尾先です！雷やられ、麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("青電主"):
        m = message.author.name + "さん！青電主は氷が効きます！弱点は通常時は頭、尾先、電荷時は尻尾、翼です！雷やられ、麻痺になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ラオシャンロン"):
        m = message.author.name + "さん！ラオシャンロンは火、龍が効きます！弱点は口内、背中です！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ラギアクルス"):
        m = message.author.name + "さん！ラギアクルスは火が効きます！弱点は頭です！雷やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("リオレイア"):
        m = message.author.name + "さん！リオレイアは龍が効きます！弱点は頭です！火やられ、毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("紫毒姫"):
        m = message.author.name + "さん！紫毒姫は龍が効きます！弱点は通常時は首、翼、尻尾、部位破壊後は背中、頭、尾先です！火やられ、毒、猛毒、劇毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("金リオレイア"):
        m = message.author.name + "さん！金リオレイアは雷が効きます！弱点は通常時は脚、部位破壊後は脚、頭です！火やられ、毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("リオレウス"):
        m = message.author.name + "さん！リオレウスは龍が効きます！弱点は頭、脚です！火やられ、毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("黒炎王"):
        m = message.author.name + "さん！黒炎王は龍が効きます！弱点は通常時は頭、首、尻尾、です！火やられ、猛毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("銀リオレウス"):
        m = message.author.name + "さん！銀リオレウスは水が効きます！弱点は脚です！火やられ、毒になる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
    if message.content.startswith("ロアルドロス"):
        m = message.author.name + "さん！ロアルドロスは火が効きます！弱点は頭です！水やられになる恐れがあります！クエストお気をつけて！"
        await message.channel.send(m)
   
   
client.run("Njg4OTk2OTgyNTcxOTI1NzE1.Xm-VZA.NLWW3UH0rEiJEDAe2fk0CfeM6fU")