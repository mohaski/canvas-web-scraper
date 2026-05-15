# Process: Advanced Tableau

# Process: Advanced Tableau

## ![](https://moringa.instructure.com/courses/1426/files/631314/preview) Process: Advanced Tableau

Icon Progress Bar (browser only)

2 min read

### Parameter Control Selector

1. **Create parameter control in Tableau.**  
   1. Set appropriate fields that correspond to desired parameters (dimensions or measures in your data).
   2. Set type (string/object or number/range).
2. **Create calculated field.**  
   1. Use CASE WHEN THEN END statements to check condition of the parameter control variable created in step 1.
   2. Assign appropriate field based on parameter selected.
   3. Include LOD dynamic calculations, if desired.
3. **Use the newly calculated field in step 2 to form visual/s.**
4. **Show Parameter on the dashboard itself to allow for user interactivity.**  
   1. Can treat this like a standard filter menu in Tableau.
   2. Visual/s should now adjust based on the selected parameter.

### Multi Dashboard Navigation

1. **Create multiple dashboards within Tableau that you want to navigate to.**  
   1. Ensure consistent styling and formatting.
2. **Drag in a navigation container to dashboard.**  
   1. Determine the navigation path (where you want it to go).
   2. Select either text display or icon/image.   
      1. See resources for free icon graphics website.
   3. Add optional tooltip (text displayed when hovered over).
3. **Add navigation buttons to all dashboards to allow for easy movement between them.**  
   1. You can pair the navigation container with a text container to provide text explanations.
   2. You can also create icon and text navigation containers to pair as well.
4. **Advanced options:**  
   1. Consider creating a ‘home page’ dashboard and home button for each dashboard.  
      1. Can treat your dashboard/s as more of a ‘website’ style.
   2. Create a dropdown menu of navigation options.  
      1. Wrap navigation containers in a single container.
      2. Add show/hide button.

---

# Source Information

Original URL: https://moringa.instructure.com/courses/1426/modules/items/248465

Scraped At: 2026-05-15T10:05:01.320168
