
apartment_type=int(input())
corporate=int(input())
bore=int(input())
no_of_guests=int(input())
new_guests=int(input())

class Bill:
    def __init__(self,type_of_apartment,corporate_water_ratio,bore_water_ratio):
        self.type_of_apartment=type_of_apartment
        self.corporate_water_ratio=corporate_water_ratio
        self.bore_water_ratio=bore_water_ratio
        self.unit_liters=0
        self.total_liters=0
        self.corporate_liters=0
        self.bore_liters=0
        self.corporate_liters_price=0
        self.bore_liters_price=0
        self.required_water_liters=0
        self.required_water_price=0
        self.total_guests=0

    def corporate_bore_liters(self):
        self.corporate_liters=self.unit_liters*self.corporate_water_ratio
        self.corporate_liters_price=self.corporate_liters*1
       
        self.bore_liters=self.unit_liters*self.bore_water_ratio
        self.bore_liters_price=self.bore_liters*1.5
        
    
    def flat_members(self):
        if self.type_of_apartment==2:
            self.total_liters=900
           
            self.unit_liters=self.total_liters/(self.corporate_water_ratio+self.bore_water_ratio)
            self.corporate_bore_liters()

        if self.type_of_apartment==3:
            self.total_liters=1500
           
            self.unit_liters=self.total_liters/(self.corporate_water_ratio+self.bore_water_ratio)
            self.corporate_bore_liters()
    

class TotalBill(Bill):
    def __init__(self, type_of_apartment, corporate_water_ratio, bore_water_ratio,guests):
        super().__init__(type_of_apartment, corporate_water_ratio, bore_water_ratio)
        self.guests=guests


    def tank_water_price(self):
        if self.required_water_liters<=500:
            self.required_water_price+=self.required_water_liters*2
        elif self.required_water_liters<=1500:
            self.required_water_price+=(500*2)+((self.required_water_liters-500)*3)
        elif self.required_water_liters<=3000:
            self.required_water_price+=(500*2)+((1500-500)*3)+((self.required_water_liters-1500)*5)
        elif self.required_water_liters>3000:
            self.required_water_price+=(500*2)+((1500-500)*3)+((3000-1500)*5)+((self.required_water_liters-3000)*8)
        
    def final_liters_prices(self):
        if self.total_guests==0:
            print(str(self.total_liters)+" "+(str(round(self.corporate_liters_price+self.bore_liters_price))))
        else:
            print(str(self.total_liters+self.required_water_liters)+" "+str(round(self.corporate_liters_price+self.bore_liters_price+self.required_water_price)))

        

    def add_guests(self,new_guests):
        self.guests+=new_guests
        
        
    
    def water_for_guests(self):
        self.total_guests+=self.guests
        self.required_water_liters+=self.total_guests*300
        self.tank_water_price()
        
        self.final_liters_prices()






bills=TotalBill(type_of_apartment=apartment_type,corporate_water_ratio=corporate,bore_water_ratio=bore,guests=no_of_guests)




bills.flat_members()
bills.add_guests(new_guests=new_guests)
bills.water_for_guests()





