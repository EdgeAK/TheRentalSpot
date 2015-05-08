from django.contrib import admin
from UserInterface.models import Director, Game, MovieGenre, GameGenre, Media, Movie, Renter, Star, MovieHasDirector
from grappelli_nested.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline



#class MyNestedInline(NestedTabularInline):
#    model = Director
#
#class AnotherNestedInline(NestedTabularInline):
#    model = MovieGenre
#    
#class MyInline(NestedStackedInline):
#    model = Movie
#    inlines = [MyNestedInline,]
#
#class MyAdmin(NestedModelAdmin):
#    model = Media
#    inlines = [MyInline,]
#
#admin.site.register(Media, MyAdmin,)

admin.site.register(Director)
admin.site.register(Game)
admin.site.register(Media)
admin.site.register(Movie)
admin.site.register(Renter)
admin.site.register(Star)
admin.site.register(GameGenre)
admin.site.register(MovieGenre)
admin.site.register(MovieHasDirector)
# Register your models here.

#from django.contrib import admin
#from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
#from models import A, B, C
#
#class MyNestedInline(NestedTabularInline):
#    model = C
#
#class MyInline(NestedStackedInline):
#    model = B
#    inlines = [MyNestedInline,]
#
#class MyAdmin(NestedModelAdmin):
#    inlines = [MyInline,]
#
#admin.site.register(A, MyAdmin)
# class StaffMemberForm(forms.ModelForm):
#    
#    def save(self, commit=True):
#    # Run the default save method, commit=False stops the
#    # model saving to the db
#        staff_member = super(StaffMemberForm, self).save(commit=False)
#
#        if self.cleaned_data.get("media_id") is None:
#            # Create a new User object
#            media_id = Media()
#
#            # Save new user
#            media_id.save()
#
#            # Apply the new user to the staff_member object
#            staff_member.media_id = media_id
#
#        else:
#            staff_member.user = self.cleaned_data.get("media_id")
#
#        # If the form was expecting to save the StaffMember then save
#        if commit:
#            staff_member.save()
#
#        return staff_member