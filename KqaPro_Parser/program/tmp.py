def exitWhatEntityQuery(self, ctx: ProgramParser.WhatEntityQueryContext):
        ctx.parentCtx.slots["query"] = "what is {}".format(self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitWhatEntityQuery(ctx)
    
    def exitHowManyEntityQuery(self, ctx: ProgramParser.HowManyEntityQueryContext):
        ctx.parentCtx.slots["query"] = "count {}".format(self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitHowManyEntityQuery(ctx)

    def exitWhatAttributeQuery(self, ctx: ProgramParser.WhatAttributeQueryContext):
        ctx.parentCtx.slots["query"] = "what is {} of {}".format(self.scoping("attribute", ctx.slots["attribute"]), self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitWhatAttributeQuery(ctx)
        
    def exitWhatRelationQuery(self, ctx: ProgramParser.WhatRelationQueryContext):
        ctx.parentCtx.slots["query"] = "what is the relation from {} to {}".format(self.scoping("entity", ctx.slots["entitySetGroup"][0]), self.scoping("entity", ctx.slots["entitySetGroup"][1]))
        return super().exitWhatRelationQuery(ctx)

    def exitSelectAmongQuery(self, ctx: ProgramParser.SelectAmongQueryContext):
        ctx.parentCtx.slots["query"] = "which one has the {} {} among {}".format(ctx.slots["selectOP"], self.scoping("attribute", ctx.slots["attribute"]), self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitSelectAmongQuery(ctx)
    
    def exitSelectBetweenQuery(self, ctx: ProgramParser.SelectBetweenQueryContext):
        ctx.parentCtx.slots["query"] = "which one has the {} {} between {} and {}".format(ctx.slots["selectOP"], self.scoping("attribute", ctx.slots["attribute"]), self.scoping("entity", ctx.slots["entitySetGroup"][0]), self.scoping("entity", ctx.slots["entitySetGroup"][1]))
        return super().exitSelectBetweenQuery(ctx)  
    
    def exitAttributeSatisfyQuery(self, ctx: ProgramParser.AttributeSatisfyQueryContext):
        ctx.parentCtx.slots["query"] = "whether {} {} {}{}".format(self.scoping("entity", ctx.slots["entitySet"]), self.scoping("attribute", ctx.slots["attribute"]), ctx.slots["verify"], ctx.slots["qualifier"])
        return super().exitAttributeSatisfyQuery(ctx)

    def exitWhatAttributeQualifierQuery(self, ctx: ProgramParser.WhatAttributeQualifierQueryContext):
        ctx.parentCtx.slots["query"] = "what is the {} of {} whose {} is {}".format(self.scoping("qualifier", ctx.slots["qualifier"]), self.scoping("entity", ctx.slots["entitySet"]), self.scoping("attribute", ctx.slots["attribute"]), self.scoping("value", ctx.slots["value"]))
        return super().exitWhatAttributeQualifierQuery(ctx)
    
    def exitWhatRelationQualifierQuery(self, ctx: ProgramParser.WhatRelationQualifierQueryContext):
        ctx.parentCtx.slots["query"] = "what is the {} of {} that {} to {}".format(self.scoping("qualifier", ctx.slots["qualifier"]), self.scoping("entity", ctx.slots["entitySetGroup"][0]), self.scoping("relation", ctx.slots["predicate"]), self.scoping("entity", ctx.slots["entitySetGroup"][1]))
        return super().exitWhatRelationQualifierQuery(ctx) 

    def exitEntitySetByOP(self, ctx: ProgramParser.EntitySetByOPContext):
        assert len(ctx.slots["entitySet"]) == 2
        self.insertParentEntitySet(ctx.parentCtx, "{} {} {}".format(self.scoping("entity", ctx.slots["entitySet"][0]), ctx.slots["setOP"], self.scoping("entity", ctx.slots["entitySet"][1])))
        return super().exitEntitySetByOP(ctx)
        
    def exitEntitySetNested(self, ctx: ProgramParser.EntitySetNestedContext):
        if ctx.slots["relationFilter"]:
            if ctx.slots["conceptFilter"]:
                self.insertParentEntitySet(ctx.parentCtx, "the {}{} {}{}".format(ctx.slots["conceptFilter"], ctx.slots["relationFilter"], ctx.slots["entitySet"], ctx.slots["qualifierFilter"]))
            else:
                self.insertParentEntitySet(ctx.parentCtx, "the one {} {}{}".format(ctx.slots["relationFilter"], self.scoping("entity", ctx.slots["entitySet"]), ctx.slots["qualifierFilter"]))
        elif ctx.slots["attributeFilter"]:
            self.insertParentEntitySet(ctx.parentCtx, "{}{} {}{}".format(ctx.slots["conceptFilter"], self.scoping("entity", ctx.slots["entitySet"]), ctx.slots["attributeFilter"], ctx.slots["qualifierFilter"]))
        return super().exitEntitySetNested(ctx)
        
    def exitEntitySetByFilter(self, ctx: ProgramParser.EntitySetByFilterContext):
        self.insertParentEntitySet(ctx.parentCtx, "{}{}{}".format(ctx.slots["conceptFilter"], ctx.slots["attributeFilter"], ctx.slots["qualifierFilter"]))
        return super().exitEntitySetByFilter(ctx)
    
    def exitEntityFilterByRelation(self, ctx: ProgramParser.EntityFilterByRelationContext):
        ctx.parentCtx.slots["relationFilter"] = "that {} {} to".format(self.scoping("relation", ctx.slots["predicate"]), ctx.slots["direction"])
        if ctx.slots["qualifier"]:
            ctx.parentCtx.slots["qualifierFilter"] = ctx.slots["qualifier"]
        if ctx.slots["concept"]:
            ctx.parentCtx.slots["conceptFilter"] = "{} ".format(self.scoping("concept", ctx.slots["concept"]))
        return super().exitEntityFilterByRelation(ctx)
      
    def exitEntityFilterByAttribute(self, ctx: ProgramParser.EntityFilterByAttributeContext):
        ctx.parentCtx.slots["attributeFilter"] = "whose {}".format(ctx.slots["attribute"])
        if ctx.slots["qualifier"]:
            ctx.parentCtx.slots["qualifierFilter"] = ctx.slots["qualifier"]
        if ctx.slots["concept"]:
            ctx.parentCtx.slots["conceptFilter"] = "{} ".format(self.scoping("concept", ctx.slots["concept"]))
        return super().exitEntityFilterByAttribute(ctx)   

    def exitEntityFilterByConcept(self, ctx: ProgramParser.EntityFilterByConceptContext):
        ctx.parentCtx.slots["conceptFilter"] = "{} ".format(self.scoping("concept", ctx.slots["concept"]))
        return super().exitEntityFilterByConcept(ctx)

    def exitFilterAttr(self, ctx: ProgramParser.FilterAttrContext):
        ctx.parentCtx.slots["attribute"] = "{} {} {} {}".format(self.scoping("attribute", ctx.slots["attribute"]), ctx.slots["OP"], ctx.slots["value_type"], self.scoping("value", ctx.slots["value"]))
        return super().exitFilterAttr(ctx)
    
    def exitFilterQualifier(self, ctx: ProgramParser.FilterQualifierContext):
        ctx.parentCtx.slots["qualifier"] = " ( {} {} {} {} )".format(self.scoping("qualifier", ctx.slots["attribute"]), ctx.slots["OP"], ctx.slots["value_type"], self.scoping("value", ctx.slots["value"]))
        return super().exitFilterQualifier(ctx)     

    def exitQueryAttributeUnderCondition(self, ctx: ProgramParser.QueryAttributeUnderConditionContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["qualifier"] = " ( {} is {} )".format("qualifier", self.scoping(ctx.slots["qkey"]), self.scoping("value", ctx.slots["qvalue"]))
        return super().exitQueryAttributeUnderCondition(ctx)
    
    def exitVerify(self, ctx: ProgramParser.VerifyContext):
        ctx.parentCtx.slots["verify"] = "{} {} {}".format(ctx.slots["OP"], ctx.slots["value_type"], self.scoping("value", ctx.slots["value"]))
        return super().exitVerify(ctx)