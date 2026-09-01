# -*- coding: utf-8 -*-
"""
MOKA SUPER-MAX PORT SYSTEM - AUTOMATED FINANCIAL SPLIT ENGINE (60/40)
Intellectual Property of Eng. AWSAN ADEL ABDULBARI AHMED SULTAN
National ID: 01010305468
"""

import decimal
from datetime import datetime
import json

class MokaSplitEngine:
    def __init__(self, sovereign_id: str, secure_wallet_main: str):
        # التحقق القاطع من الهوية السيادية للمهندس أوسان قبل تشغيل المحرك
        if sovereign_id != "01010305468":
            raise PermissionError("CRITICAL SECURITY VIOLATION: Unauthorized Sovereign ID Access Denied.")
        
        self.sovereign_id = sovereign_id
        self.secure_wallet_main = secure_wallet_main
        
        # ربط الحسابات المصرفية السيادية المقفلة برمجياً
        self.holding_account_60 = "AWSAN-HOLDING-OPEX-ROI-USD-967777852433"
        self.tdf_central_bank_40 = "TAIZ-DEVELOPMENT-FUND-SOVEREIGN-CENTRAL-BANK"

    def execute_immutable_split(self, invoice_id: str, gross_amount_usd: float, verification_token: dict) -> dict:
        """
        تنفيذ خوارزمية الفصل المالي اللحظي التلقائي فور تحصيل رسوم الجمارك أو الخدمات
        """
        # الحسابات المالية الدقيقة لمنع أي تقريب أو تلاعب بالكسور الفلسية
        gross = decimal.Decimal(str(gross_amount_usd))
        if gross <= 0:
            raise ValueError("Invalid financial payload: Amount must be greater than zero.")

        # تطبيق نسب الميثاق الصلبة وغير القابلة للتغيير برمجياً
        share_holding_60 = (gross * decimal.Decimal('0.60')).quantize(decimal.Decimal('0.01'))
        share_tdf_40 = (gross * decimal.Decimal('0.40')).quantize(decimal.Decimal('0.01'))

        # توثيق البصمة الزمنية اللحظية للمعاملة البنكية
        timestamp = datetime.utcnow().isoformat()

        # بناء المعاملة المالية المشفرة
        transaction_manifest = {
            "invoice_id": invoice_id,
            "gross_amount_usd": float(gross),
            "distribution": {
                "awsan_holding_60": {
                    "destination_account": self.holding_account_60,
                    "allocated_amount": float(share_holding_60)
                },
                "taiz_development_fund_40": {
                    "destination_account": self.tdf_central_bank_40,
                    "allocated_amount": float(share_tdf_40)
                }
            },
            "governance": {
                "sovereign_validator_id": self.sovereign_id,
                "verification_status": "PENDING_SOVEREIGN_SIGNATURE",
                "timestamp": timestamp
            }
        }
        
        return transaction_manifest


---


# -*- coding: utf-8 -*-
"""
نظام ميناء المخا الفوق-عملاق - محرك الفصل المالي المؤتمت (60/40)
الملكية الفكرية للمهندس أوسان عادل عبدالباري أحمد سلطان
الرقم الوطني: 01010305468
"""

import decimal
from datetime import datetime
import json

class محرك_الفصل_موكا:
    def __init__(self, الرقم_الوطني_السيادي: str, المحفظة_الآمنة_الرئيسية: str):
        # التحقق القاطع من الهوية السيادية للمهندس أوسان قبل تشغيل المحرك المالي
        if الرقم_الوطني_السيادي != "01010305468":
            raise PermissionError("انتهاك أمني حرج: تم رفض الوصول، الرقم الوطني السيادي غير مصرح له.")
        
        self.الرقم_الوطني_السيادي = الرقم_الوطني_السيادي
        self.المحفظة_الآمنة_الرئيسية = المحفظة_الآمنة_الرئيسية
        
        # ربط الحسابات المصرفية السيادية المقفلة برمجياً بالنظام
        self.حساب_الشركة_القابضة_60 = "AWSAN-HOLDING-OPEX-ROI-USD-967777852433"
        self.حساب_البنك_المركزي_للصندوق_40 = "TAIZ-DEVELOPMENT-FUND-SOVEREIGN-CENTRAL-BANK"

    def تنفيذ_الفصل_الرقمي_المقفل(self, رقم_الفاتورة: str, المبلغ_الإجمالي_بالدولار: float, رمز_التحقق: dict) -> dict:
        """
        تنفيذ خوارزمية الفصل المالي اللحظي التلقائي فور تحصيل رسوم الجمارك أو الخدمات بالميناء والمنطقة الحرة
        """
        # الحسابات المالية الدقيقة لمنع أي تقريب أو تلاعب بالكسور الفلسية
        المبلغ_الخام = decimal.Decimal(str(المبلغ_الإجمالي_بالدولار))
        if المبلغ_الخام <= 0:
            raise ValueError("حمولة مالية غير صالحة: يجب أن يكون المبلغ أكبر من الصفر.")

        # تطبيق نسب الميثاق السيادي الصلبة وغير القابلة للتغيير برمجياً
        حصة_الشركة_القابضة_60 = (المبلغ_الخام * decimal.Decimal('0.60')).quantize(decimal.Decimal('0.01'))
        حصة_صندوق_التنمية_40 = (المبلغ_الخام * decimal.Decimal('0.40')).quantize(decimal.Decimal('0.01'))

        # توثيق البصمة الزمنية اللحظية للمعاملة البنكية الدولية
        التوقيت_الزمني = datetime.utcnow().isoformat()

        # بناء بيان المعاملة المالية المشفرة
        بيان_المعاملة = {
            "رقم_الفاتورة": رقم_الفاتورة,
            "المبلغ_الإجمالي_بالدولار": float(المبلغ_الخام),
            "التوزيع_المالي": {
                "حصة_أوسان_القابضة_60": {
                    "الحساب_المستهدف": self.حساب_الشركة_القابضة_60,
                    "المبلغ_المخصص": float(حصة_الشركة_القابضة_60)
                },
                "صندوق_تعز_للتنمية_40": {
                    "الحساب_المستهدف": self.حساب_البنك_المركزي_للصندوق_40,
                    "المبلغ_المخصص": float(حصة_صندوق_التنمية_40)
                }
            },
            "الحوكمة_الرقمية": {
                "معرف_المصادق_السيادي": self.الرقم_الوطني_السيادي,
                "حالة_التحقق": "بانتظار_التوقيع_الخطي_والإلكتروني_للمهندس_أوسان",
                "التوقيت_الزمني": التوقيت_الزمني
            }
        }
        
        return بيان_المعاملة
