from .. import *


@sbb_b.ar_cmd(pattern="الاوامر")
async def hi(event):
    await event.reply(
        "**[ . ᯏ𝖩𝗆𝗍𝗁𝗈ꪀ - ᥴ𝗆𝖽 ᭡ .](t.me/AKJA0)\n✦┅━╍━╍╍━━╍━━╍━┅✦**\n\n**- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس **\n\n`.الامر1` ◂ اوامر الأدمن\n`.الامر2` ◂ اوامر المجموعة\n`.م3` ◂ اوامر الترحيب\n`.م4` ◂ اوامر الردود\n`.م5` ◂ اوامر الترفيه\n`.م6` ◂ اوامر حماية الخاص\n`.م7` ◂ اوامر الاذاعه و الكشف \n`.م8` ◂ اوامر البوت \n`.م9` ◂ اوامر المنع والترجمه\n`.م10` ◂ اوامر التلكراف و النطق\n`.م11` ◂ اوامر التحميل\n`.م12` ◂ اوامر التكرار\n`.م13` ◂ اوامر الانتحال والتقليد\n`.م14` ◂ اوامر الوقتي \n`.م15` ◂ اوامر الذاتيه والاضافه\n`.م16` ◂ اوامر البروفايل\n`.م17` ◂ اوامر الأكسترا\n`.م18` ◂ التاك و الملفات\n`.م19` ◂  اوامر الفارات\n`.م20` ◂  اوامر التسلية",
        link_preview=False,
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="الامر1")
async def hi(event):
    await event.reply(
        "**قائـمه اوامر الادمن :**\n◂  `.حظر` \n❃ لحظر الشخص في مجموعه بالرد عليه\n\n ◂  `.الغاء الحظر`\n❃ لالغاء حظر الشخص من المجموعه بالرد عليه\n\n ◂  `.كتم` \n❃ لكتم الشخص بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.الغاء كتم`\n❃ لالغاء كتم الشخص بالرد عليه بالامر\n\n ◂  `.تثبيت` \n❃ بالرد على الرسالة لتثبيتها في المجموعة\n\n ◂  `.الغاء التثبيت` \n❃ لألغاء تثبيت الرسالة في المجموعة \n\n ◂  `.رفع مشرف`  < لقب > \n❃ بالرد ؏ المستخدم لرفعه مشرف يمكنك وضع لقب\n\n ◂  `.تنزيل مشرف` \n❃ بالرد ؏ المستخدم لتنزيله من المشرفين\n\n ◂  `.ارفع`\n❃ بالرد ؏ المستخدم لرفعه مشرف في جميع المجموعات \n\n ◂  `.نزل`\n❃ بالرد ؏ المستخدم لتنزيله من جميع المجموعات\n\n ◂  `.الاحداث`\n❃ فقط ارسل الامر لعرض اخر احداث المجموعه \n\n ◂  `.حذف المحظورين`\n❃ لالغاء جميع المحظورين في المجموعه فقط اكتب الامر\n\n ◂  `.المحذوفين`\n❃ لعرض الحسابات المحذوفة في المجموعه فقط اكتب الامر\n\n ◂  `.تفليش`\n❃ لحظر جميع المستخدمين من المجموعه فقط اكتب الامر\n\n ◂  `.تنزيل الكل`\n❃ لتنزيل جميع المشرفين من المجموعه فقط ارسل الامر في المجموعه\n\n ◂  `.المحظورين`\n❃ لعرض المستخدمين المحظورين في المجموعه اكتب الامر فقط\n\n ◂  `.تحذير`\n❃ بالرد على المستخدم لتحذيره في المجموعه \n\n ◂  `.حذف التحذيرات`\nلحذف تحذيرات المستخدم بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.التحذيرات`\n❃ بالرد على المستخدم لعرض عدد تحذيراته"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="الامر2")
async def hi(event):
    await event.reply(
        "قائمـه اوامر المجموعة :\n\n ◂  `.المشرفين` \n❃ فقط اكتب الامر في المجموعه لعرض مشرفين المجموعه\n\n ◂  `.البوتات` \n❃ فقط اكتب الامر في الدردشة لعرض البوتات المضافة \n\n ◂  `.الاعضاء`\n❃ فقط اكتب الامر في المجموعه لعرض أعضاء الدردشة\n\n ◂  `.معلومات`\n❃ لعرض معلومات المجموعه اكتبه الامر في المجموعة"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م3")
async def hi(event):
    await event.reply(
        "قائمـه اوامر الترحيب :\n\n ◂  `.ترحيب`\n❃ اكتب الامر مع الترحيب ليقوم بالترحيب في المستخدمين الجدد في المجموعة\n\n ◂  `.الترحيب`\n❃ لعرض رساله الترحيب الحاليه اكتب الامر فقط\n\n ◂  `.الغاء الترحيب`\n❃ لالغاء الترحيب في المستخدمين فقط اكتب الامر\n\n⌔∮ متغيرات الترحيب [اضغط هنا](https://t.me/JJOTT/4)",
        link_preview=False,
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م4")
async def hi(event):
    await event.reply(
        "قائمـه اوامر الردود :\n\n ◂  `.رد`\n❃ يستخدم الأمر بإضافة رد في المجموعه اكتب الامر والرد الخاص بك بالرد على الكلمه \n\n ◂  `.حذف الردود`\n❃ فقط اكتب الامر في الدردشه لحذف جميع الردود المضافه\n\n ◂  `.الردود`\n❃ لعرض الردود المصافه فقط اكتب الامر\n\n ◂  `.ايقاف`\n❃ اكتب الامر مع الرد لحذف الرد من الدردشه\n\n⌔∮ شرح توضيحي عن اوامر الردود  [اضغط هنا](https://telegra.ph/اوامر-جمثون-04-24)\n⌔∮ شرح عن متغيرات الردود  [اضغط هنا](https://t.me/JJOTT/20)",
        link_preview=False,
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م5")
async def hi(event):
    await event.reply(
        "**قائـمه اوامر الترفيه:**\n\n• جميع هذه الاوامر تستخدم بالرد على الشخص كترفيه\n ◂  `.رفع مطي`\n ◂  `.رفع كلب`\n ◂  `.رفع حيوان`\n ◂  `.رفع زاحف`\n ◂  `.رفع مرتي`\n ◂  `.رفع زوجي`\n ◂  `.رفع تاج`\n ◂  `.رفع بكلبي`\n ◂  `.رفع بزون`\n ◂  `.رفع قرد`\n\n ◂  `.نسبة الحب`\n ◂  `.نسبة الانوثة`\n ◂  `.نسبة الرجولة`\n ◂  `.نسبة الغباء`\n ◂  `.نسبة المثْلية`\n\n ◂  `.كت`\n ◂  `.اوصف`\n ◂  `.هينه`\n ◂  `.نزوج`\n ◂  `.طلاك`"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م6")
async def hi(event):
    await event.reply(
        "قائمـه اوامر حماية الخاص :\n\n ◂  `.الحماية تشغيل`\n❃ لتشغيل امر الحمايه يستخدم لتحذير المستخدمين عند مراسلتك في الخاص من التكرار\n\n ◂  `.الحماية تعطيل`\n❃ لتعطيل امر الحمايه وعدم تحذير المستخدمين في الخاص\n\n ◂  `.سماح` او `.س`\n❃ يستخدم الامر لقبول الشخص في الخاص وعدم ارسال تحذيرات له بالرد على الشخص\n\n ◂  `.رفض` او `.ر`\n❃ يستخدم لرفض الشخص من الخاص وتحذيره اذا كرر الرسائل وبعدها حظره\n\n ◂  `.بلوك`\n❃ بالرد على المستخدم لحظره من الخاص\n\n ◂  `.انبلوك`\n❃ بالرد على المستخدم لالغاء حظره من الخاص\n\n ◂  `.المسموح لهم`\n❃ اكتب الامر فقط لعرض معلومات عن الاشخاص الذين قبلته في الخاص\n\n⌔∮ لعرض فارات الحماية ارسل `.الفارات`",
        link_preview=False,
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م7")
async def hi(event):
    await event.reply(
        "قائمـه اوامر الكشف والاذاعة  :\n\n ◂  `.ايدي`\n❃ بالرد على المستخدم او وضع معرفه مع الامر لعرض معلوماته\n\n ◂  `.كشف`\n❃ بالرد على المستخدم لعرض معلومات معينه عنه\n\n ◂  `.للخاص`\n❃ اكتب الامر بالرد على رساله او اي ميديا ليقوم بارساله لجميع المحادثات في الخاص\n\n ◂  `.للكروبات`\n❃ بالرد على نص او اي ميديا ليقوم بنشره في جمبع المجموعات\n\n⌔∮ متغيرات الايدي  [اضغط هنا](https://t.me/JJOTT/20)",
        link_preview=False,
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م8")
async def hi(event):
    await event.reply(
        "قائمـه اوامر البوت :\n\n ◂  `.فحص`\n❃ فقط اكتب الامر لعرض معلومات السورس\n\n ◂  `.السورس`\n❃ فقط اكتب الامر لعىض معلومات عن السورس\n\n ◂  `.بنك`\n❃ فقط اكتب الامر لعرض سرعه البوت\n\n ◂  `.الانترنت + الاضافه`\n❃ يستخدم الامر لقياس سرعه البوت اكتب الامر مع الاضافه  :  `.الانترنت صورة`  `.الانترنت نص`\n\n ◂  `.اعادة تشغيل`\n❃ لعمل اعادة تشغيل للسورس وتحديثه \n\n ◂  `.الاشعارات` + تشغيل/تعطيل\n❃ لتشغيل او تعطيل الاشعارات عند تحديث او اعادة تشغيل السورس"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م9")
async def hi(event):
    await event.reply(
        "قائمـه اوامر المنع والترجمة :\n\n ◂  `.منع`\n❃ اكتب الاكر مع الكلمه لمنع ارساله في المجموعه او اي دردشه\n\n ◂  `.الغاء منع`\n❃ اكتب الامر مع الكلمه لالغاء منعها من الدردشه\n\n ◂  `.قائمة المنع`\n❃ اكتب الامر لعرض قائمه الكلمات التي منعتها في الدردشة\n\n ◂  `.ترجمة`\n❃ يستخدم الاكر لترجمه الكلمات اكتب الامر مع كود اللغه بالرد غلى النص لترجمته\n\n⌔∮ اكواد اللغات للترجمه  [اضغط هنا](https://telegra.ph/اكواد-اللغه-للترجمه-04-24)"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م10")
async def hi(event):
    await event.reply(
        "قائمـه اوامر التلكراف و النطق :\n\n ◂  `.انطق`\n❃ بالرد على الكلام لتسجيله ببصمه و ارساله لك\n\n ◂  `.تلكراف ميديا ◂  \n❃ بالرد على الميديا لصنع رابط تلكراف منها\n\n ◂  `.تلكراف نص`\n❃ بالرد على النص لعمل رابط تلكراف"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م11")
async def hi(event):
    await event.reply(
        "قائمـه اوامر التحميل :\n\n ◂  `.تحميل فيديو`\n❃ بالرد على رابط من يوتيوب او اي موقع ثاني لتحميل الفيديو وارساله لك\n\n ◂  `.تحميل صوتي`\n❃ اكتب الامر بالرد على الرابط من اليوتيوب لتكميل مقطع الصوتي و ارساله لك\n\n ◂  `.انستا`\n❃ اكتب الامر بالرد على الرابط التحميل من الانستا \n\n ◂  `.بينترست`\n❃ بالرد على رابط من بينتسرت للتحميل لك\n\n ◂  `.صور`\n❃ اكتب الامر مع عنوان للبحث عنه وارسال لك الصور،  اذا بحثت عن اباحي سيتم تعطيل حسابك"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م12")
async def hi(event):
    await event.reply(
        "** قائـمه اوامر التكرار**:\n\n◂ `.كرر`\n❃ اكتب الامر مع عدد التكرار بالرد ؏ النص او او صورة ملصق ليقوم بتكراره مع العدد الذي وضعته\n\n ◂  `.تكرار الملصق` \n❃ بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها في الدردشة\n\n ◂ `.مكرر`\n❃ اكتب الامر مع وقت بالثواني و مع عدد التكرار وبالرد على صورة او نص  (  تكرار وقتي  )\n\n ◂  `.التكرار`\n❃ بالرد على الرسالة بالامر فقط سيقوم بعمل تكرار سريع ويصل عدده الى 10 الاف تكرار  ! \n\n ◂  `.ايقاف التكرار`\n❃ يقوم هذا الامر بأيقاف التكرار فقط اكتبه\n\n** تنبيه اوامر التكرار قد تؤدي الى حظر حسابك على التلي اذا استخدمتها بشكل غير صحيح**"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م13")
async def hi(event):
    await event.reply(
        "** قائـمه اوامر الأنتحال و التقليد :**\n\n ◂  `.انتحال`\n❃ بالرد على المستخدم لأنتحال حسابه  من اسم وصورة وبايو  . \n\n ◂  `.اعادة`\n❃ لأعادة حسابك الى وضعه السابق  .\n\n ◂ `.تقليد`\n❃ بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n ◂ `.الغاء تقليد`\n❃ بالرد على الشخص لايقاف التقليد\n\n ◂ `.المقلدهم `\n❃ لاظهار قائمه الاشخاص الذي فعلت عليهم امر التقليد ولمسحهم ارسل  `.حذف المقلدهم`"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م14")
async def hi(event):
    await event.reply(
        "قائـمه اوامر الوقتي:**\n\n◂ `.اسم وقتي`\n❃ بكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها \n\n ◂ `.انهاء اسم وقتي`\n❃ لانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\n ◂ `.بايو وقتي`\n❃ بكتابة الامر لاضافة ساعه يتحرك مع النبذة الخاصة بك  \n\n ◂ `.انهاء بايو وقتي`\n❃ لانهاء البايو الوقتي و ارجاع البايو الطبيعي\n\n ◂  `.الصورة الوقتية`\n❃ لبدء تشغيل وقت على الصورة الخاصة بحسابك\n\n ◂  `.انهاء الصورة الوقتية`\n❃ لألغاء امر الصورة الوقتية"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م15")
async def hi(event):
    await event.reply(
        "اوامر جلب الذاتية وامر الاضافة**:\n\n ◂  `.ضيف`\n❃ اكتب الامر مع رابط مجموعه التي تريد سحب اعضائها وارسل الامر في مجموعتك لسحبهم الى مجموعتك\n\n ◂ `.جلب الصورة`  او  `.ذاتية`\n❃ بالرد على صورة او فيديو ذاتية التدمير لحفظها وارسالها في الرسائل المحفوظة بسرية تامة الامر لجمثون حصريا!"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م16")
async def hi(event):
    await event.reply(
        "قائـمه اوامر البروفايل: \n\n ◂  `.تغيير اسم`\n❃ لتغيير اسم حسابك اكتب الاسم مع الامر\n\n ◂  `.تغيير بايو`\n❃ لتغيير بايو حسابك اكتب البايو مع الامر \n\n ◂  `.تغيير صورة`\n❃ لتغيير صورة حسابك بالرد على الصورة بالامر\n\n ◂  `.تغيير معرف`\n❃ لتغيير معرف حسابك اكتب المعرف مع الامر\n\n ◂  `.ازاله الصورة`\n❃ اكبت الامر لحذف صورة حسابك\n\n ◂  `.معرفاتي`\n❃ لعرض معرفات حسابك التي صنعتها\n\n ◂  `.حسابي`\n❃ لعرض معلومات و احصائيات حسابك"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م17")
async def hi(event):
    await event.reply(
        "قائـمه اوامر الأكسترا: \n\n ◂  `.الرابط`\n❃ لجلب رابط المجموعه يجب ان تكون مشرف \n\n ◂  `.الحاسبة`\n❃ لعرض حاسبه علميه جربه بنفسك\n\n ◂  `.حالتي`\n❃ لعرض حاله حسابك الحاليه اذا كان محظور او لا\n\n ◂  `.صلاة`❃ اكتب الامر مع اسم محافظتك او مدينتك بالانكليزي لعرض اوقات الصلاة والامساك\n\n ◂  `.تغميق`\n❃ بالرد على الكلام لجعله بشكل غامق\n\n ◂  `.نسخ`\n❃ بالرد على الكلام لجعله بشكل للنسخ\n\n ◂  `.مائل`\n❃ بالرد على الكلام لجعله بشكل مائل"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م18")
async def hi(event):
    await event.reply(
        "قائـمه اوامر التاك والملفات:\n\n ◂  `.للكل`  او  `.تاك للكل`\n❃ لعمل تاك لاخر 100 عضو في المجموعه اكتب الامر مع اي نص تريد\n\n ◂  `.تبليغ`\n❃ لتبليغ المشرفين اذا حصل شيء ما فقط اكتب الامر\n\n ◂  `.منشن`\n❃ بالرد على المستخدم وكتابه شيء مع الامر لعمل تاك داخل الكلمه للمستخدم\n\n ◂  `.تنصيب`\n❃ لتنصيب ملفات خارجيه للسورس \n\n ◂  `.الغاء تنصيب`\n❃ بكتابه الامر مع اسم الملف لحذف تنصيبه من السورس"
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م19")
async def hi(event):
    await event.reply(
        "قائـمه اوامر الفارات:\n\n ◂  `.وضع رمز الاسم`\n❃ بالرد على رمز لوضعه قرب اسمك عند تفعيل امر اسم وقتي\n\n ◂  `.اضف صورة الحماية`\n❃ بالرد على رابط الصورة لوضعها لامر الحماية لحذف الفار ارسل `.حذف صورة الحماية`\n\n ◂  `.اضف صورة الفحص`\n❃ بالرد على رابط الصورة لوضعها لامر الفحص لحذف الفار ارسل `.حذف صورة الفحص` \n\n◂  `.وضع البايو`\n❃ بالرد على البايو لوضعه لحسابك عند تشغيل امر بايو وقتي\n\n ◂  `.وضع الصورة`\n❃ بالرد على رابط صورة تلكراف لوضعها صورة حسابك عند تشغيل امر الصورة الوقتية\n\n ◂  `.وضع زخرفة الارقام`\n❃ بالرد على ارقام مزخرفه لوضعها كزخرفه لارقام امر الاسم الوقتي يجب ان يكون الارقام على هذا التسلسل 𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎\n\n ◂  `.وضع الاسم`\n❃ بالرد على اسم لوضعه اسم لحسابك يستخدم في العديد من الاوامر \n\n ◂  `.وضع كروب التخزين`\n❃ بالرد على ايدي مجموعتك لوضعها كمجموعه تخزين لتخزين رسائل الخاص بها انتبه يجب ان يكزن الكروب خاص بك فقط\n\n\n ◂  `.اضف كليشة الحماية`\n❃ بالرد على كليشه لوضعها كـكليشه حمايه خاصه بك لحذف الفار ارسل `.حذف كليشة الحماية`\n⌔∮ متغيرات و كلايش الحمايه [اضغط هنا](https://t.me/JJOTT/7)\n\n ◂  `.اضف كليشة الفحص`\n❃ بالرد على كليشه لوضع كليشه لامر الفحص الخاص بك لحذف الفار ارسل `.حذف كليشة الفحص`\n⌔∮ متغيرات و كلايش الفحص [اضغط هنا](https://t.me/JJOTT/72)\n\n ◂  `.اضف كليشة الحظر`\n❃ بالرد على كليشه لاضافه كليشه عند حظر شخص بامر الحمايه \n\n ◂  `.اضف ايموجي الفحص`\n❃ بالرد على رمز او ايموجي لوضعه بكليشه الفحص\n\n ◂  `.اضف عدد التحذيرات`\n\n❃ لتغيير عدد التحذيرات الخاصه بحسابك قبل حظر الشخص في امر الحمايه\n\n ◂  `.وقت العراق`  او `.وقت مصر` او  `.وقت اليمن` او  `.وقت الاردن` او  `.وقت سوريا`\n❃ لتغيير الوقت الخاص بك حسب دولتك فقط ارسل وان لم تكن دولتك موجوده هنا استخدم امر  `.توقيت` بالرد غلى المنطقه الزمنيه الخاصه بك",
        link_preview=False,
    )
    await event.delete()


@sbb_b.ar_cmd(pattern="م20")
async def hi(event):
    await event.reply(
        "**⌔∮ قائـمة اوامر التسلية**: \\n\n`.غبي`  `.القنابل`  `.اتصل`   `.قتل`    `.طوبة`\n\n`.مربعات`   `.حلويات`     `.نار`     `.شحن`\n\n`.افكر`    `.متت`    `.ضايج`    `.ساعة`\n\n`.مح`    `.قلب`     `.جيم`     `.الارض`\n\n`.قمر`      `.اقمار`     `.قمور `    `.نجمه`\n\n`.مكعبات`   `.مطر `     `.تفريغ`      `.فليم`\n\n`.احبك`    `.طائره`        `.شرطه `\n\n`.النضام الشمسي`    `.قاتل`       `.عين`\n\n`.افكرر`      `.افعى`         `.رج`      `.مايكرو`\n\n`.فايروس`    `.قطار`      `.موسيقى `\n\n`.رسم`   `.تحميل`     `.مربع`       `.دائره`\n\n`.انيم`    `.بشره`      `.قرد`      `.يد`\n\n`.العد التنازلي`        `.قلوب`\n\n`.فصخ + الكلام`\n\n`.تهكير`     `.تهكير2`   `.تهكير3`\n\nٴ╼──────────────────╾\n • جميع الاوامر تستخدم بالضغط على الامر راح ينسخ وحده وارسله فقط"
    )
    await event.delete()
