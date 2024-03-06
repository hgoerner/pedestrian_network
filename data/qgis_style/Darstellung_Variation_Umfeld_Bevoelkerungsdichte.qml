<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis simplifyDrawingTol="1" simplifyMaxScale="1" version="3.22.11-Białowieża" simplifyDrawingHints="1" simplifyAlgorithm="0" hasScaleBasedVisibilityFlag="0" maxScale="0" labelsEnabled="0" symbologyReferenceScale="-1" styleCategories="AllStyleCategories" readOnly="0" simplifyLocal="1" minScale="100000000">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal limitMode="0" startField="" endField="" startExpression="" durationField="fid" durationUnit="min" fixedDuration="0" enabled="0" accumulate="0" endExpression="" mode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 enableorderby="0" referencescale="-1" type="RuleRenderer" forceraster="0" symbollevels="0">
    <rules key="{4f97d7a0-597b-4fa2-b9e8-f8b0db5887fa}">
      <rule symbol="0" key="{8b229902-b22f-4e62-a842-cba875f3c6db}" label="UH_BH" filter="&quot;Summe Poi*Bedeutung je km&quot; > 440 AND &quot;Einwohner-Faktor&quot; > 0.5">
        <rule symbol="1" key="{32ccbe4d-eb29-4933-8538-ba0daea04311}" label="Umfeld Niedrig" filter="&quot;Summe Poi*Bedeutung je km&quot; > 440 AND &quot;Summe Poi*Beudeutung je km&quot; &lt; 610"/>
        <rule symbol="2" key="{ee7ad117-b475-4fc5-bc19-e4deec7b4b30}" label="Umfeld Mittel" filter="&quot;Summe Poi*Bedeutung je km&quot; > 610 AND &quot;Summe Poi*Beudeutung je km&quot; &lt; 1574"/>
        <rule symbol="3" key="{13c58dad-59ce-4e4e-9313-2c15f284d5bd}" label="Umfeld Hoch" filter="&quot;Summe Poi*Bedeutung je km&quot; > 1574"/>
      </rule>
      <rule symbol="4" key="{c90074fc-d550-436a-80d7-cedd18bb97c4}" label="UH_BN" filter="&quot;Summe Poi*Bedeutung je km&quot; > 440 AND &quot;Einwohner-Faktor&quot; &lt; 0.5">
        <rule symbol="5" key="{94683ed8-d3c1-4ed5-aa3b-03cb271b0693}" label="Umfeld Niedrig" filter="&quot;Summe Poi*Bedeutung je km&quot; > 440 AND &quot;Summe Poi*Beudeutung je km&quot; &lt; 610"/>
        <rule symbol="6" key="{1a07aa31-5e0c-4f7a-bb55-dc2e5fae599b}" label="Umfeld Mittel" filter="'&quot;Summe Poi*Bedeutung je km&quot; > 610 AND &quot;Summe Poi*Beudeutung je km&quot; &lt; 1574'"/>
        <rule symbol="7" key="{4ac1d07f-5f70-40e1-aabb-07ad2b225fd7}" label="Umfeld Hoch" filter="&quot;Summe Poi*Bedeutung je km&quot; > 1574"/>
      </rule>
      <rule symbol="8" key="{83fc69ac-2e59-472d-b04c-61630265f7c6}" label="UN_BH" filter="&quot;Summe Poi*Bedeutung je km&quot; &lt; 440 AND &quot;Einwohner-Faktor&quot; > 0.5">
        <rule symbol="9" key="{89fd87ba-5792-49ea-90d4-efa7ef1d576a}" label="Umfeld Hoch" filter="&quot;Summe Poi*Bedeutung je km&quot; > 270 AND &quot;Summe Poi*Beudeutung je km&quot; &lt; 440"/>
        <rule symbol="10" key="{c587c628-d2a7-441b-a6bd-cb92920c2bc6}" label="Umfeld Mittel" filter="'&quot;Summe Poi*Bedeutung je km&quot; &lt; 270 AND &quot;Summe Poi*Beudeutung je km&quot; > 105'"/>
        <rule symbol="11" key="{aefed0a5-3aad-4ed1-845c-6a07a39cc1b7}" label="Umfeld Niedrig" filter="&quot;Summe Poi*Bedeutung je km&quot; &lt; 105"/>
      </rule>
      <rule symbol="12" key="{6e2f1567-df8a-44e9-b83d-a1f0df9a6e68}" label="UN_BN" filter="&quot;Summe Poi*Bedeutung je km&quot; &lt; 440 AND &quot;Einwohner-Faktor&quot; &lt; 0.5">
        <rule symbol="13" key="{b75523a8-0a0d-4d91-9f7b-204fea0ec841}" label="Umfeld Hoch" filter="&quot;Summe Poi*Bedeutung je km&quot; > 270 AND &quot;Summe Poi*Beudeutung je km&quot; &lt; 440"/>
        <rule symbol="14" key="{c439362a-eee8-41f8-8df2-053a816ad13c}" label="Umfeld Mittel" filter="&quot;Summe Poi*Bedeutung je km&quot; &lt; 270 AND &quot;Summe Poi*Beudeutung je km&quot; > 105"/>
        <rule symbol="15" key="{0b33099d-6743-4971-a7e8-5491f233632b}" label="Umfeld Niedrig" filter="&quot;Summe Poi*Bedeutung je km&quot; &lt; 105"/>
      </rule>
    </rules>
    <symbols>
      <symbol force_rhr="0" alpha="1" name="0" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="255,31,1,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,31,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="1" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="0,21,254,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,21,254,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="10" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="31,255,1,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="31,255,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="11" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="0,21,254,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,21,254,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="12" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="1,213,255,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="1,213,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="13" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="255,54,71,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,54,71,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="14" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="31,255,1,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="31,255,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="15" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="0,21,254,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,21,254,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="2" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="31,255,1,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="31,255,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="3" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="255,54,71,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,54,71,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="4" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="255,149,1,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,149,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="5" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="0,21,254,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,21,254,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="6" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="31,255,1,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="31,255,1,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="7" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="255,54,71,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,54,71,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="8" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="1,52,255,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="1,52,255,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol force_rhr="0" alpha="1" name="9" clip_to_extent="1" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" enabled="1" locked="0" pass="0">
          <Option type="Map">
            <Option value="0" name="align_dash_pattern" type="QString"/>
            <Option value="square" name="capstyle" type="QString"/>
            <Option value="5;2" name="customdash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
            <Option value="MM" name="customdash_unit" type="QString"/>
            <Option value="0" name="dash_pattern_offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
            <Option value="0" name="draw_inside_polygon" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="255,54,71,255" name="line_color" type="QString"/>
            <Option value="solid" name="line_style" type="QString"/>
            <Option value="0.26" name="line_width" type="QString"/>
            <Option value="MM" name="line_width_unit" type="QString"/>
            <Option value="0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="0" name="ring_filter" type="QString"/>
            <Option value="0" name="trim_distance_end" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_end_unit" type="QString"/>
            <Option value="0" name="trim_distance_start" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
            <Option value="MM" name="trim_distance_start_unit" type="QString"/>
            <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
            <Option value="0" name="use_custom_dash" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="255,54,71,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <Option type="Map">
      <Option value="true" name="OnConvertFormatRegeneratePrimaryKey" type="bool"/>
      <Option name="dualview/previewExpressions" type="List">
        <Option value="&quot;full_id&quot;" type="QString"/>
      </Option>
      <Option value="0" name="embeddedWidgets/count" type="int"/>
      <Option name="variableNames"/>
      <Option name="variableValues"/>
    </Option>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory spacingUnit="MM" sizeScale="3x:0,0,0,0,0,0" diagramOrientation="Up" showAxis="1" rotationOffset="270" lineSizeType="MM" labelPlacementMethod="XHeight" enabled="0" spacing="5" lineSizeScale="3x:0,0,0,0,0,0" direction="0" maxScaleDenominator="1e+08" backgroundAlpha="255" scaleBasedVisibility="0" minScaleDenominator="0" sizeType="MM" barWidth="5" height="15" minimumSize="0" spacingUnitScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" opacity="1" scaleDependency="Area" penColor="#000000" penAlpha="255" penWidth="0" width="15">
      <fontProperties style="" description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0"/>
      <attribute field="" label="" colorOpacity="1" color="#000000"/>
      <axisSymbol>
        <symbol force_rhr="0" alpha="1" name="" clip_to_extent="1" type="line">
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
          <layer class="SimpleLine" enabled="1" locked="0" pass="0">
            <Option type="Map">
              <Option value="0" name="align_dash_pattern" type="QString"/>
              <Option value="square" name="capstyle" type="QString"/>
              <Option value="5;2" name="customdash" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale" type="QString"/>
              <Option value="MM" name="customdash_unit" type="QString"/>
              <Option value="0" name="dash_pattern_offset" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale" type="QString"/>
              <Option value="MM" name="dash_pattern_offset_unit" type="QString"/>
              <Option value="0" name="draw_inside_polygon" type="QString"/>
              <Option value="bevel" name="joinstyle" type="QString"/>
              <Option value="35,35,35,255" name="line_color" type="QString"/>
              <Option value="solid" name="line_style" type="QString"/>
              <Option value="0.26" name="line_width" type="QString"/>
              <Option value="MM" name="line_width_unit" type="QString"/>
              <Option value="0" name="offset" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
              <Option value="MM" name="offset_unit" type="QString"/>
              <Option value="0" name="ring_filter" type="QString"/>
              <Option value="0" name="trim_distance_end" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale" type="QString"/>
              <Option value="MM" name="trim_distance_end_unit" type="QString"/>
              <Option value="0" name="trim_distance_start" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale" type="QString"/>
              <Option value="MM" name="trim_distance_start_unit" type="QString"/>
              <Option value="0" name="tweak_dash_pattern_on_corners" type="QString"/>
              <Option value="0" name="use_custom_dash" type="QString"/>
              <Option value="3x:0,0,0,0,0,0" name="width_map_unit_scale" type="QString"/>
            </Option>
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="trim_distance_end"/>
            <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
            <prop v="MM" k="trim_distance_end_unit"/>
            <prop v="0" k="trim_distance_start"/>
            <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
            <prop v="MM" k="trim_distance_start_unit"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings placement="2" linePlacementFlags="18" dist="0" priority="0" zIndex="0" obstacle="0" showAll="1">
    <properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <legend showLabelLegend="0" type="default-vector"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="fid" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="full_id" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="osm_id" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Wohnen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Bildungseinrichtungen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Oeffentliche Gebaeude*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Haltestellen des OPNV*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Gesundheit*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Einwohnerschwerpunkte*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Altenpflegeheime*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Kindergaerten*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Grundschulen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="weiterefuehrende Schulen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Hochschulen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Geschaefte*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="grossflaechiger Einzelhandel*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Gastronomie*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Bibliotheken &amp; Post*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Polizei &amp; Justiz*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Sportanlagen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Spielplaetze*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Baeder*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Grossveranstaltungen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Hotels, Pensionen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Bushaltestelle*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Strassenbahnhaltestelle*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="SPNV-Haltestelle*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Krankenhaeuser*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Friedhof*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Wald/Gehoelz*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Kleingarten*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Platz*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Gewaesser*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Park/gestaltetes Gruen*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Einwohner" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Summe Poi*Bedeutung" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Laenge" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Einwohner je km" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Einwohner-Faktor" configurationFlags="None">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="Summe Poi*Bedeutung je km" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="full_id" index="1" name=""/>
    <alias field="osm_id" index="2" name=""/>
    <alias field="Wohnen*Bedeutung" index="3" name=""/>
    <alias field="Bildungseinrichtungen*Bedeutung" index="4" name=""/>
    <alias field="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" index="5" name=""/>
    <alias field="Oeffentliche Gebaeude*Bedeutung" index="6" name=""/>
    <alias field="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" index="7" name=""/>
    <alias field="Haltestellen des OPNV*Bedeutung" index="8" name=""/>
    <alias field="Gesundheit*Bedeutung" index="9" name=""/>
    <alias field="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" index="10" name=""/>
    <alias field="Einwohnerschwerpunkte*Bedeutung" index="11" name=""/>
    <alias field="Altenpflegeheime*Bedeutung" index="12" name=""/>
    <alias field="Kindergaerten*Bedeutung" index="13" name=""/>
    <alias field="Grundschulen*Bedeutung" index="14" name=""/>
    <alias field="weiterefuehrende Schulen*Bedeutung" index="15" name=""/>
    <alias field="Hochschulen*Bedeutung" index="16" name=""/>
    <alias field="Geschaefte*Bedeutung" index="17" name=""/>
    <alias field="grossflaechiger Einzelhandel*Bedeutung" index="18" name=""/>
    <alias field="Gastronomie*Bedeutung" index="19" name=""/>
    <alias field="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" index="20" name=""/>
    <alias field="Bibliotheken &amp; Post*Bedeutung" index="21" name=""/>
    <alias field="Polizei &amp; Justiz*Bedeutung" index="22" name=""/>
    <alias field="Sportanlagen*Bedeutung" index="23" name=""/>
    <alias field="Spielplaetze*Bedeutung" index="24" name=""/>
    <alias field="Baeder*Bedeutung" index="25" name=""/>
    <alias field="Grossveranstaltungen*Bedeutung" index="26" name=""/>
    <alias field="Hotels, Pensionen*Bedeutung" index="27" name=""/>
    <alias field="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" index="28" name=""/>
    <alias field="Bushaltestelle*Bedeutung" index="29" name=""/>
    <alias field="Strassenbahnhaltestelle*Bedeutung" index="30" name=""/>
    <alias field="SPNV-Haltestelle*Bedeutung" index="31" name=""/>
    <alias field="Krankenhaeuser*Bedeutung" index="32" name=""/>
    <alias field="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" index="33" name=""/>
    <alias field="Friedhof*Bedeutung" index="34" name=""/>
    <alias field="Wald/Gehoelz*Bedeutung" index="35" name=""/>
    <alias field="Kleingarten*Bedeutung" index="36" name=""/>
    <alias field="Platz*Bedeutung" index="37" name=""/>
    <alias field="Gewaesser*Bedeutung" index="38" name=""/>
    <alias field="Park/gestaltetes Gruen*Bedeutung" index="39" name=""/>
    <alias field="Einwohner" index="40" name=""/>
    <alias field="Summe Poi*Bedeutung" index="41" name=""/>
    <alias field="Laenge" index="42" name=""/>
    <alias field="Einwohner je km" index="43" name=""/>
    <alias field="Einwohner-Faktor" index="44" name=""/>
    <alias field="Summe Poi*Bedeutung je km" index="45" name=""/>
  </aliases>
  <defaults>
    <default field="fid" applyOnUpdate="0" expression=""/>
    <default field="full_id" applyOnUpdate="0" expression=""/>
    <default field="osm_id" applyOnUpdate="0" expression=""/>
    <default field="Wohnen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Bildungseinrichtungen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Oeffentliche Gebaeude*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Haltestellen des OPNV*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Gesundheit*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Einwohnerschwerpunkte*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Altenpflegeheime*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Kindergaerten*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Grundschulen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="weiterefuehrende Schulen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Hochschulen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Geschaefte*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="grossflaechiger Einzelhandel*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Gastronomie*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Bibliotheken &amp; Post*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Polizei &amp; Justiz*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Sportanlagen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Spielplaetze*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Baeder*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Grossveranstaltungen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Hotels, Pensionen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Bushaltestelle*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Strassenbahnhaltestelle*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="SPNV-Haltestelle*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Krankenhaeuser*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Friedhof*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Wald/Gehoelz*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Kleingarten*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Platz*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Gewaesser*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Park/gestaltetes Gruen*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Einwohner" applyOnUpdate="0" expression=""/>
    <default field="Summe Poi*Bedeutung" applyOnUpdate="0" expression=""/>
    <default field="Laenge" applyOnUpdate="0" expression=""/>
    <default field="Einwohner je km" applyOnUpdate="0" expression=""/>
    <default field="Einwohner-Faktor" applyOnUpdate="0" expression=""/>
    <default field="Summe Poi*Bedeutung je km" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint field="fid" unique_strength="1" exp_strength="0" notnull_strength="1" constraints="3"/>
    <constraint field="full_id" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="osm_id" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Wohnen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Bildungseinrichtungen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Oeffentliche Gebaeude*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Haltestellen des OPNV*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Gesundheit*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Einwohnerschwerpunkte*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Altenpflegeheime*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Kindergaerten*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Grundschulen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="weiterefuehrende Schulen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Hochschulen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Geschaefte*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="grossflaechiger Einzelhandel*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Gastronomie*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Bibliotheken &amp; Post*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Polizei &amp; Justiz*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Sportanlagen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Spielplaetze*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Baeder*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Grossveranstaltungen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Hotels, Pensionen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Bushaltestelle*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Strassenbahnhaltestelle*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="SPNV-Haltestelle*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Krankenhaeuser*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Friedhof*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Wald/Gehoelz*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Kleingarten*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Platz*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Gewaesser*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Park/gestaltetes Gruen*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Einwohner" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Summe Poi*Bedeutung" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Laenge" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Einwohner je km" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Einwohner-Faktor" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
    <constraint field="Summe Poi*Bedeutung je km" unique_strength="0" exp_strength="0" notnull_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" field="fid" exp=""/>
    <constraint desc="" field="full_id" exp=""/>
    <constraint desc="" field="osm_id" exp=""/>
    <constraint desc="" field="Wohnen*Bedeutung" exp=""/>
    <constraint desc="" field="Bildungseinrichtungen*Bedeutung" exp=""/>
    <constraint desc="" field="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" exp=""/>
    <constraint desc="" field="Oeffentliche Gebaeude*Bedeutung" exp=""/>
    <constraint desc="" field="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" exp=""/>
    <constraint desc="" field="Haltestellen des OPNV*Bedeutung" exp=""/>
    <constraint desc="" field="Gesundheit*Bedeutung" exp=""/>
    <constraint desc="" field="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" exp=""/>
    <constraint desc="" field="Einwohnerschwerpunkte*Bedeutung" exp=""/>
    <constraint desc="" field="Altenpflegeheime*Bedeutung" exp=""/>
    <constraint desc="" field="Kindergaerten*Bedeutung" exp=""/>
    <constraint desc="" field="Grundschulen*Bedeutung" exp=""/>
    <constraint desc="" field="weiterefuehrende Schulen*Bedeutung" exp=""/>
    <constraint desc="" field="Hochschulen*Bedeutung" exp=""/>
    <constraint desc="" field="Geschaefte*Bedeutung" exp=""/>
    <constraint desc="" field="grossflaechiger Einzelhandel*Bedeutung" exp=""/>
    <constraint desc="" field="Gastronomie*Bedeutung" exp=""/>
    <constraint desc="" field="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" exp=""/>
    <constraint desc="" field="Bibliotheken &amp; Post*Bedeutung" exp=""/>
    <constraint desc="" field="Polizei &amp; Justiz*Bedeutung" exp=""/>
    <constraint desc="" field="Sportanlagen*Bedeutung" exp=""/>
    <constraint desc="" field="Spielplaetze*Bedeutung" exp=""/>
    <constraint desc="" field="Baeder*Bedeutung" exp=""/>
    <constraint desc="" field="Grossveranstaltungen*Bedeutung" exp=""/>
    <constraint desc="" field="Hotels, Pensionen*Bedeutung" exp=""/>
    <constraint desc="" field="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" exp=""/>
    <constraint desc="" field="Bushaltestelle*Bedeutung" exp=""/>
    <constraint desc="" field="Strassenbahnhaltestelle*Bedeutung" exp=""/>
    <constraint desc="" field="SPNV-Haltestelle*Bedeutung" exp=""/>
    <constraint desc="" field="Krankenhaeuser*Bedeutung" exp=""/>
    <constraint desc="" field="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" exp=""/>
    <constraint desc="" field="Friedhof*Bedeutung" exp=""/>
    <constraint desc="" field="Wald/Gehoelz*Bedeutung" exp=""/>
    <constraint desc="" field="Kleingarten*Bedeutung" exp=""/>
    <constraint desc="" field="Platz*Bedeutung" exp=""/>
    <constraint desc="" field="Gewaesser*Bedeutung" exp=""/>
    <constraint desc="" field="Park/gestaltetes Gruen*Bedeutung" exp=""/>
    <constraint desc="" field="Einwohner" exp=""/>
    <constraint desc="" field="Summe Poi*Bedeutung" exp=""/>
    <constraint desc="" field="Laenge" exp=""/>
    <constraint desc="" field="Einwohner je km" exp=""/>
    <constraint desc="" field="Einwohner-Faktor" exp=""/>
    <constraint desc="" field="Summe Poi*Bedeutung je km" exp=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="1" actionWidgetStyle="dropDown" sortExpression="&quot;Summe Poi*Beudeutung je km&quot;">
    <columns>
      <column hidden="0" name="fid" type="field" width="-1"/>
      <column hidden="0" name="Wohnen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Bildungseinrichtungen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Oeffentliche Gebaeude*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Haltestellen des OPNV*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Gesundheit*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Einwohnerschwerpunkte*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Altenpflegeheime*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Kindergaerten*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Grundschulen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Hochschulen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Geschaefte*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="grossflaechiger Einzelhandel*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Gastronomie*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Sportanlagen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Spielplaetze*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Baeder*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Grossveranstaltungen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Hotels, Pensionen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Bushaltestelle*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Strassenbahnhaltestelle*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="SPNV-Haltestelle*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Krankenhaeuser*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Friedhof*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Wald/Gehoelz*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Kleingarten*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Platz*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Gewaesser*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Einwohner" type="field" width="-1"/>
      <column hidden="0" name="Laenge" type="field" width="-1"/>
      <column hidden="0" name="Einwohner je km" type="field" width="-1"/>
      <column hidden="0" name="Einwohner-Faktor" type="field" width="-1"/>
      <column hidden="0" name="full_id" type="field" width="-1"/>
      <column hidden="0" name="osm_id" type="field" width="-1"/>
      <column hidden="0" name="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="weiterefuehrende Schulen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Bibliotheken &amp; Post*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Polizei &amp; Justiz*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Park/gestaltetes Gruen*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Summe Poi*Bedeutung" type="field" width="-1"/>
      <column hidden="0" name="Summe Poi*Bedeutung je km" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS-Formulare können eine Python-Funktion haben,, die aufgerufen wird, wenn sich das Formular öffnet

Diese Funktion kann verwendet werden um dem Formular Extralogik hinzuzufügen.

Der Name der Funktion wird im Feld "Python Init-Function" angegeben
Ein Beispiel folgt:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name=" Summe Poi*Bedeutung je km"/>
    <field editable="1" name="Altenpflegeheime*Bedeutung"/>
    <field editable="1" name="Baeder*Bedeutung"/>
    <field editable="1" name="Bibliotheken &amp; Post*Bedeutung"/>
    <field editable="1" name="Bibliotheken und Post*Bedeutung"/>
    <field editable="1" name="Bildungseinrichtungen*Bedeutung"/>
    <field editable="1" name="Bushaltestelle*Bedeutung"/>
    <field editable="1" name="Dienstleistung, Einzelhandel, Gastromie*Bedeutung"/>
    <field editable="1" name="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung"/>
    <field editable="1" name="Dienstleistungen, Einzelhandel und Gastronomie*Bedeutung"/>
    <field editable="1" name="Einwohner"/>
    <field editable="1" name="Einwohner je km"/>
    <field editable="1" name="Einwohner*Bedeutung"/>
    <field editable="1" name="Einwohner-Faktor"/>
    <field editable="1" name="Einwohnerschwerpunkte*Bedeutung"/>
    <field editable="1" name="Friedhof*Bedeutung"/>
    <field editable="1" name="Gastronomie*Bedeutung"/>
    <field editable="1" name="Geschaefte*Bedeutung"/>
    <field editable="1" name="Gesundheit*Bedeutung"/>
    <field editable="1" name="Gewaesser*Bedeutung"/>
    <field editable="1" name="Grossveranstaltungen*Bedeutung"/>
    <field editable="1" name="Gruen, Blau und Platzflaechen*Bedeutung"/>
    <field editable="1" name="Gruen-, Blau- &amp; Platzflaechen*Bedeutung"/>
    <field editable="1" name="Gruen-, Blau- und Platzflaechen*Bedeutung"/>
    <field editable="1" name="Grundschulen*Bedeutung"/>
    <field editable="1" name="Haltestellen des OPNV*Bedeutung"/>
    <field editable="1" name="Hochschulen*Bedeutung"/>
    <field editable="1" name="Hotels, Pensionen*Bedeutung"/>
    <field editable="1" name="Kindergaerten*Bedeutung"/>
    <field editable="1" name="Kleingarten*Bedeutung"/>
    <field editable="1" name="Krankenhaeuser*Bedeutung"/>
    <field editable="1" name="Laenge"/>
    <field editable="1" name="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung"/>
    <field editable="1" name="Oeffentliche Gebaeude*Bedeutung"/>
    <field editable="1" name="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung"/>
    <field editable="1" name="Oeffentliche Verwaltung und Buergeraemter*Bedeutung"/>
    <field editable="1" name="Park/gestaltes Gruen*Bedeutung"/>
    <field editable="1" name="Park/gestaltetes Gruen*Bedeutung"/>
    <field editable="1" name="Platz*Bedeutung"/>
    <field editable="1" name="Polizei &amp; Justiz*Bedeutung"/>
    <field editable="1" name="Polizei und Justiz*Bedeutung"/>
    <field editable="1" name="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung"/>
    <field editable="1" name="SPNV-Haltestelle*Bedeutung"/>
    <field editable="1" name="Spielplaetze*Bedeutung"/>
    <field editable="1" name="Sportanlagen*Bedeutung"/>
    <field editable="1" name="Strassenbahnhaltestelle*Bedeutung"/>
    <field editable="1" name="Summe  Poi*Beudeutung"/>
    <field editable="1" name="Summe POI*Bedeutung"/>
    <field editable="1" name="Summe Poi*Bedeutung"/>
    <field editable="1" name="Summe Poi*Bedeutung je km"/>
    <field editable="1" name="Summe Poi*Beudeutung"/>
    <field editable="1" name="Summe Poi*Beudeutung je km"/>
    <field editable="1" name="Versammlungsstaetten, Sport und Freizeit*Bedeutung"/>
    <field editable="1" name="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung"/>
    <field editable="1" name="Wald/Gehoelz*Bedeutung"/>
    <field editable="1" name="Wohnen*Bedeutung"/>
    <field editable="1" name="fid"/>
    <field editable="1" name="full_id"/>
    <field editable="1" name="grossflaechiger Einzelhandel*Bedeutung"/>
    <field editable="1" name="osm_id"/>
    <field editable="1" name="weiterefuehrende Schulen*Bedeutung"/>
    <field editable="1" name="weiterfuehrende Schulen*Bedeutung"/>
  </editable>
  <labelOnTop>
    <field name=" Summe Poi*Bedeutung je km" labelOnTop="0"/>
    <field name="Altenpflegeheime*Bedeutung" labelOnTop="0"/>
    <field name="Baeder*Bedeutung" labelOnTop="0"/>
    <field name="Bibliotheken &amp; Post*Bedeutung" labelOnTop="0"/>
    <field name="Bibliotheken und Post*Bedeutung" labelOnTop="0"/>
    <field name="Bildungseinrichtungen*Bedeutung" labelOnTop="0"/>
    <field name="Bushaltestelle*Bedeutung" labelOnTop="0"/>
    <field name="Dienstleistung, Einzelhandel, Gastromie*Bedeutung" labelOnTop="0"/>
    <field name="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung" labelOnTop="0"/>
    <field name="Dienstleistungen, Einzelhandel und Gastronomie*Bedeutung" labelOnTop="0"/>
    <field name="Einwohner" labelOnTop="0"/>
    <field name="Einwohner je km" labelOnTop="0"/>
    <field name="Einwohner*Bedeutung" labelOnTop="0"/>
    <field name="Einwohner-Faktor" labelOnTop="0"/>
    <field name="Einwohnerschwerpunkte*Bedeutung" labelOnTop="0"/>
    <field name="Friedhof*Bedeutung" labelOnTop="0"/>
    <field name="Gastronomie*Bedeutung" labelOnTop="0"/>
    <field name="Geschaefte*Bedeutung" labelOnTop="0"/>
    <field name="Gesundheit*Bedeutung" labelOnTop="0"/>
    <field name="Gewaesser*Bedeutung" labelOnTop="0"/>
    <field name="Grossveranstaltungen*Bedeutung" labelOnTop="0"/>
    <field name="Gruen, Blau und Platzflaechen*Bedeutung" labelOnTop="0"/>
    <field name="Gruen-, Blau- &amp; Platzflaechen*Bedeutung" labelOnTop="0"/>
    <field name="Gruen-, Blau- und Platzflaechen*Bedeutung" labelOnTop="0"/>
    <field name="Grundschulen*Bedeutung" labelOnTop="0"/>
    <field name="Haltestellen des OPNV*Bedeutung" labelOnTop="0"/>
    <field name="Hochschulen*Bedeutung" labelOnTop="0"/>
    <field name="Hotels, Pensionen*Bedeutung" labelOnTop="0"/>
    <field name="Kindergaerten*Bedeutung" labelOnTop="0"/>
    <field name="Kleingarten*Bedeutung" labelOnTop="0"/>
    <field name="Krankenhaeuser*Bedeutung" labelOnTop="0"/>
    <field name="Laenge" labelOnTop="0"/>
    <field name="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung" labelOnTop="0"/>
    <field name="Oeffentliche Gebaeude*Bedeutung" labelOnTop="0"/>
    <field name="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung" labelOnTop="0"/>
    <field name="Oeffentliche Verwaltung und Buergeraemter*Bedeutung" labelOnTop="0"/>
    <field name="Park/gestaltes Gruen*Bedeutung" labelOnTop="0"/>
    <field name="Park/gestaltetes Gruen*Bedeutung" labelOnTop="0"/>
    <field name="Platz*Bedeutung" labelOnTop="0"/>
    <field name="Polizei &amp; Justiz*Bedeutung" labelOnTop="0"/>
    <field name="Polizei und Justiz*Bedeutung" labelOnTop="0"/>
    <field name="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung" labelOnTop="0"/>
    <field name="SPNV-Haltestelle*Bedeutung" labelOnTop="0"/>
    <field name="Spielplaetze*Bedeutung" labelOnTop="0"/>
    <field name="Sportanlagen*Bedeutung" labelOnTop="0"/>
    <field name="Strassenbahnhaltestelle*Bedeutung" labelOnTop="0"/>
    <field name="Summe  Poi*Beudeutung" labelOnTop="0"/>
    <field name="Summe POI*Bedeutung" labelOnTop="0"/>
    <field name="Summe Poi*Bedeutung" labelOnTop="0"/>
    <field name="Summe Poi*Bedeutung je km" labelOnTop="0"/>
    <field name="Summe Poi*Beudeutung" labelOnTop="0"/>
    <field name="Summe Poi*Beudeutung je km" labelOnTop="0"/>
    <field name="Versammlungsstaetten, Sport und Freizeit*Bedeutung" labelOnTop="0"/>
    <field name="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung" labelOnTop="0"/>
    <field name="Wald/Gehoelz*Bedeutung" labelOnTop="0"/>
    <field name="Wohnen*Bedeutung" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="full_id" labelOnTop="0"/>
    <field name="grossflaechiger Einzelhandel*Bedeutung" labelOnTop="0"/>
    <field name="osm_id" labelOnTop="0"/>
    <field name="weiterefuehrende Schulen*Bedeutung" labelOnTop="0"/>
    <field name="weiterfuehrende Schulen*Bedeutung" labelOnTop="0"/>
  </labelOnTop>
  <reuseLastValue>
    <field reuseLastValue="0" name=" Summe Poi*Bedeutung je km"/>
    <field reuseLastValue="0" name="Altenpflegeheime*Bedeutung"/>
    <field reuseLastValue="0" name="Baeder*Bedeutung"/>
    <field reuseLastValue="0" name="Bibliotheken &amp; Post*Bedeutung"/>
    <field reuseLastValue="0" name="Bibliotheken und Post*Bedeutung"/>
    <field reuseLastValue="0" name="Bildungseinrichtungen*Bedeutung"/>
    <field reuseLastValue="0" name="Bushaltestelle*Bedeutung"/>
    <field reuseLastValue="0" name="Dienstleistung, Einzelhandel, Gastromie*Bedeutung"/>
    <field reuseLastValue="0" name="Dienstleistung, Einzelhandel, Gastronomie*Bedeutung"/>
    <field reuseLastValue="0" name="Dienstleistungen, Einzelhandel und Gastronomie*Bedeutung"/>
    <field reuseLastValue="0" name="Einwohner"/>
    <field reuseLastValue="0" name="Einwohner je km"/>
    <field reuseLastValue="0" name="Einwohner*Bedeutung"/>
    <field reuseLastValue="0" name="Einwohner-Faktor"/>
    <field reuseLastValue="0" name="Einwohnerschwerpunkte*Bedeutung"/>
    <field reuseLastValue="0" name="Friedhof*Bedeutung"/>
    <field reuseLastValue="0" name="Gastronomie*Bedeutung"/>
    <field reuseLastValue="0" name="Geschaefte*Bedeutung"/>
    <field reuseLastValue="0" name="Gesundheit*Bedeutung"/>
    <field reuseLastValue="0" name="Gewaesser*Bedeutung"/>
    <field reuseLastValue="0" name="Grossveranstaltungen*Bedeutung"/>
    <field reuseLastValue="0" name="Gruen, Blau und Platzflaechen*Bedeutung"/>
    <field reuseLastValue="0" name="Gruen-, Blau- &amp; Platzflaechen*Bedeutung"/>
    <field reuseLastValue="0" name="Gruen-, Blau- und Platzflaechen*Bedeutung"/>
    <field reuseLastValue="0" name="Grundschulen*Bedeutung"/>
    <field reuseLastValue="0" name="Haltestellen des OPNV*Bedeutung"/>
    <field reuseLastValue="0" name="Hochschulen*Bedeutung"/>
    <field reuseLastValue="0" name="Hotels, Pensionen*Bedeutung"/>
    <field reuseLastValue="0" name="Kindergaerten*Bedeutung"/>
    <field reuseLastValue="0" name="Kleingarten*Bedeutung"/>
    <field reuseLastValue="0" name="Krankenhaeuser*Bedeutung"/>
    <field reuseLastValue="0" name="Laenge"/>
    <field reuseLastValue="0" name="Museen, Gebaeude mit ueberoertlicher Bedeutung*Bedeutung"/>
    <field reuseLastValue="0" name="Oeffentliche Gebaeude*Bedeutung"/>
    <field reuseLastValue="0" name="Oeffentliche Verwaltung &amp; Buergeraemter*Bedeutung"/>
    <field reuseLastValue="0" name="Oeffentliche Verwaltung und Buergeraemter*Bedeutung"/>
    <field reuseLastValue="0" name="Park/gestaltes Gruen*Bedeutung"/>
    <field reuseLastValue="0" name="Park/gestaltetes Gruen*Bedeutung"/>
    <field reuseLastValue="0" name="Platz*Bedeutung"/>
    <field reuseLastValue="0" name="Polizei &amp; Justiz*Bedeutung"/>
    <field reuseLastValue="0" name="Polizei und Justiz*Bedeutung"/>
    <field reuseLastValue="0" name="Praxen, Gesundheitsbedarf, Sozialeinrichtungen*Bedeutung"/>
    <field reuseLastValue="0" name="SPNV-Haltestelle*Bedeutung"/>
    <field reuseLastValue="0" name="Spielplaetze*Bedeutung"/>
    <field reuseLastValue="0" name="Sportanlagen*Bedeutung"/>
    <field reuseLastValue="0" name="Strassenbahnhaltestelle*Bedeutung"/>
    <field reuseLastValue="0" name="Summe  Poi*Beudeutung"/>
    <field reuseLastValue="0" name="Summe POI*Bedeutung"/>
    <field reuseLastValue="0" name="Summe Poi*Bedeutung"/>
    <field reuseLastValue="0" name="Summe Poi*Bedeutung je km"/>
    <field reuseLastValue="0" name="Summe Poi*Beudeutung"/>
    <field reuseLastValue="0" name="Summe Poi*Beudeutung je km"/>
    <field reuseLastValue="0" name="Versammlungsstaetten, Sport und Freizeit*Bedeutung"/>
    <field reuseLastValue="0" name="Versammlungsstaetten, Sport- &amp; Freizeit*Bedeutung"/>
    <field reuseLastValue="0" name="Wald/Gehoelz*Bedeutung"/>
    <field reuseLastValue="0" name="Wohnen*Bedeutung"/>
    <field reuseLastValue="0" name="fid"/>
    <field reuseLastValue="0" name="full_id"/>
    <field reuseLastValue="0" name="grossflaechiger Einzelhandel*Bedeutung"/>
    <field reuseLastValue="0" name="osm_id"/>
    <field reuseLastValue="0" name="weiterefuehrende Schulen*Bedeutung"/>
    <field reuseLastValue="0" name="weiterfuehrende Schulen*Bedeutung"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"full_id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>1</layerGeometryType>
</qgis>
