
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = []
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
    def add_member(self, first_name, age, lucky_numbers, id=None):
        # fill this method and update the return
        member = {
            "id": id if id else self._generateId(),
            "first_name" : first_name,
            "last_name": "Jackson",
            "age" : age,
            "lucky_numbers" : lucky_numbers
        }
        self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        pass
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return {"done": True}
        return {"error": f"Member with id {id} not found."}

    def get_member(self, id):
        # fill this method and update the return
        pass
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
