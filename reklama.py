######################################################################################
##############################################################################
#✅✅STATIC YA'NI VAQTINCHALIK XOTIRA BILAN TELEGRAMDA 'MAVZU', 'REKLAMA MATINI' VA ' RASIM '  HAMDA
 # BOSHQA O'ZINGIZ UCHUN KERAKLI MA'LUMOTLARNI  ALOHIDA ADMIN TAMONIDAN KIRITIB, BITTA REKLAMA QILIB OBUNACHILARGA YUBORISH,

 #✅✅ BUNDA SIZ BIR VAQTDA IKKITA ISHNI  YA'NI  REKLAMANI YASAYSIZ VA REKLAMANI OBUNACHILARGA YETKAZASIZ.

# 
# ✅✅✅ SIZ AYNAN SHU KO'RINISHDA FILE,  BIR NECHTA RASIM, MATIN, REKLAMA MAVZUSI YOKI NOMINI, LINKINI, TELFON RAQAMINI, MANZILINI VA
 # SHUNGA O'XSHASH XOHLAGAN MA'LUMOTLARINGIZNI KIRITIB BITTA REKLAMA YASASHINGIZ MUMKIN BO'LADI.
 ######################################################################################
####################################################################################################################################################################
##############################################################################
@dp.message_handler(commands="reklama", state="*",user_id=admin)
async def send_welcome(message: types.Message,  state: FSMContext):
    await message.answer("✅Reklama mavzusi yoki nomini kiriting!!!")  
    await state.set_state(StateData.name_r)  ############# BU YERDA BOTGA ADMIN /REKLAMA BUYRUG'INI YUBORSA RAKLAMA NOMINI BILISH UCHUN "NOMI YOKI MAVZUSI" DEB SO'RAYDI, VA VAQTINCH KIRITILGAN MAVZU YOKI NOMINI SAQLAB TURADI.
   


@dp.message_handler(state=StateData.name_r)
async def echo(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer("✅Iltimos  matin ko'rinishida kiriting")
        return
    await state.update_data(name_r=message.text)
    await message.answer("✅Reklamaning asosiy matinini kiriting!!! ")
    await StateData.next() ###################### BU YERRDA AGAR NOMINI O'RNIGA FAQAT RAQAM YOKI BELGI, RASIM, FILE TASHLASA NOMINI MATIN KO'RINISHIDA TSHLANG DEB QAYTA SO'RAYDI, YA'NI QABUL QILMAYDI, TO'G'RI KIRITILGANDAN SO'NG REKLAMA UCHUN ASOSIY MATN SO'RALADI.


@dp.message_handler(state=StateData.description_r)
async def echo(message: types.Message, state: FSMContext):
    if message.text.isalpha():
        await message.answer("✅Iltimos reklama asosiy matinini matin ko'rinishida kiriting")
        return
    await state.update_data(description_r=message.text)
    await message.answer("✅Iltimos  reklamaga oid biror rasim yuklang!!!\n('jpg') ")
    await StateData.next() ############################ BU YERDA HAM REKLAMA ASOSIY MATININI MATIN KO'RINISHIDA YUBORMAGUNCHA QABUL QILMAYDI, SO'NG REKLAMAGA OID RASIM SO'RAYDI.

    



@dp.message_handler(content_types="any", state=StateData.photo_r)
async def echo(message: types.Message, state: FSMContext):
    if message.content_type != "photo":
        await message.answer("rasimni jpg farmatda kiriting")
        return
    await state.update_data(photo_r=message.photo[-1]['file_id'])
    data = await state.get_data()

    name_r_ = data.get("name_r")
    description_r_ = data.get("description_r")
    photo_r_ = data.get("photo_r") ########### RASIM O'RNIGA BOSHQA NARSA TASHLASA QABUL QILMAYDI.
 ########## BU YERDAGI name_r_, description_r_, photo_r lar static filedagi vaqtincha saqlangan ma'lulotlar
    

    users = db.select_users_all() ####### bu yerdagi db.select_users_all DATA BASEDAGI OBUNACHILAR IDSINI OLIB BERADI.
    for user in users:
        tel_id = user[0]
        await bot.send_photo(chat_id=tel_id,photo=photo_r_,caption=f"""📚$$$✅Reklama: {name_r_}
✅HURMATLI OBUNACHI {description_r_}
🤝✅Mening boshqa loyhalarim;\n\t👨‍💻✅ @dilshodbeK_arimov kanalimda✅✅ \n👌✅ALBATTA OBUNA BO'LING!!!""")
############# RASIMNI TOG'RI TASHLAGANDAN SO'NG HAMMASINI BIRLASHTIRIB SIZGA OBUNACHILARGA YUBORADI.


 ######################################################################################
####################################################################################################################################################################
##############################################################################
 ######################################################################################
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
# ✅✅✅✅ DATA BASE VA STATIC FILENI ULASH VA ULAR BILAN ISHLASH, ULARDAGI KODLARNI MENGA YOZSANGIZ TASHLAB BERMAN 
# ✅✅✅✅ TUSHUNMAGAN JOYINGIZNI SO'RANG. https://t.me/XDK16 LICHKAM https://t.me/dilshodbeK_arimov TELEGRAM KANAL
# ✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
####################################################################################################################################################################
##############################################################################
 ######################################################################################
####################################################################################################################################################################
##############################################################################
