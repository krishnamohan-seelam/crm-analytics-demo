import tomli
import streamlit as st
import utils
import mock_data
from sidebar import SideBarController, SideBarModel, SideBarView
from mainpage import Header, KPIMetrics, ChartsSection


def display_page_title():
    st.set_page_config(
        page_title="CRM Campaign Dashboard",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def display_title():
    st.title(f"CRM Campaign Dashboard")


def main(dry_run=False):
    display_page_title()
    # display_title()
    if dry_run:
        side_bar_data = utils.load_data(utils.FAKE_DATA_PATH)

    # sidebar = SideBar(data=side_bar_data)

    # selected_agent,selected_polling_booth  = sidebar.render_content()
    sb_model = SideBarModel(side_bar_data)
    sb_view = SideBarView()
    sb_controller = SideBarController(sb_model, sb_view)
    sb_controller.show_sidebar()

    # st.write("constituency name" + sb_controller.model.constituency_name)
    # st.write("You have selected polling booth " + sb_controller.polling_booth)
    # st.write("You have selected polling agent " + sb_controller.agent)

    constituency_map = {"constituency_name": [sb_controller.model.constituency_name]}
    polling_booth_map = {"polling_booth": [sb_controller.polling_booth]}
    agent_map = {"agent_name": [sb_controller.agent]}

    header = Header(constituency_map, polling_booth_map, agent_map)
    header.render()
    first_metrics = KPIMetrics(mock_data.layer_01_metrics)
    first_metrics.render()
    second_metrics = KPIMetrics(mock_data.layer_02_metrics)
    second_metrics.render()
    charts_section = ChartsSection(
        mock_data.charts_metrics,
        mock_data.gauge_metrics,
        mock_data.table_metrics,
        mock_data.piechart_metrics,
    )
    charts_section.render()


if __name__ == "__main__":
    utils.add_app_path()
    config = utils.load_config(utils.TOML_CONFIG_PATH)

    utils.validate_config(config)
    main(config.get("dry_run"))
